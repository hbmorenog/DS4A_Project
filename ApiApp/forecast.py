# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 08:11:58 2021

@author: dusty
"""
from flask_restful import Resource,reqparse

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
        
        data={"Message":args['date']}
        return data

