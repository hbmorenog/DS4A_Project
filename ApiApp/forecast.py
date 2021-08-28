# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 08:11:58 2021

@author: dusty
"""
from flask_restful import Resource,reqparse
from psycopg_util import Pyscopg_util
from lstm_model import Lstm_model
from sklearn import linear_model
import pandas as pd
import numpy as np
class Forecast(Resource):
    def post(self):
        #initialize
        parser= reqparse.RequestParser()
        #add args
        parser.add_argument('date',required=True)
        parser.add_argument('model',required=True)
        parser.add_argument('period',required=True)
        #parse args to dict
        args=parser.parse_args()
        try:
            util=Pyscopg_util()
            util.connect_to_db()
            if args['period']=="daily":
                chunk_size=1
            if args['period']=="weekly":
                chunk_size=7
            if args['period']=="monthly":
                chunk_size=30
            if args['period']=="yearly":
                chunk_size=365
            data=util.select_demanda_energia_forecast(date=args['date'],chunk_size=chunk_size)
        finally:
            util.close_connection()
        if args['model']== 'linear_regression':
            forecast_df=pd.DataFrame()
            for i in range(14):
                X= np.arange(14).reshape(-1,1)
                Y= data.iloc[i:i+14]
                model = linear_model.LinearRegression().fit(X, Y)
                linear_model.LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
                Y_pred = model.predict(X[13].reshape(-1,1))
                serie=pd.Series({'Real':data.iloc[i+14]['promedio'],'Expected':Y_pred[0][0]},name=data.index.values[i+14])
                forecast_df=forecast_df.append(serie)
            print(forecast_df)
            return forecast_df.to_dict()
        if args['model']== 'lstm':
            model=Lstm_model()
            try:
                util=Pyscopg_util()
                util.connect_to_db()
                demanda_energia=util.select_demanda_energia(date=args['date'],chunk_size=chunk_size)
            finally:
                 util.close_connection()
            initial_date=demanda_energia.index.values[0]
            final_date=args['date']
            X1=demanda_energia['Demanda']
            X2=data.iloc[0:15]['promedio']
            dpred=model.make_prediction(X1,X2,initial_date,final_date)
            dpred.insert(1, "real", data['promedio'].to_list()[14:], True)
            dpred.index=dpred.index.strftime("%Y-%m-%d")
            return dpred.to_dict()
            
   
    
