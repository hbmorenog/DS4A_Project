# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 07:55:54 2021

@author: dusty
"""
import sys
from flask_restful import Resource,reqparse
from psycopg_util import Pyscopg_util
class Data(Resource):
    
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
            data=util.select_demanda_energia(date=args['date'])
            return data
        finally:
            util.close_connection()
    def get(self):
        data={"Message":"Holi"}
        return data
