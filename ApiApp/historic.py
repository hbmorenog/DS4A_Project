# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 07:55:54 2021

@author: dusty
"""
from flask_restful import Resource,reqparse
from psycopg_util import Pyscopg_util
class Historic(Resource):
    
    def post(self):
        #initialize
        parser= reqparse.RequestParser()
        #add args
        parser.add_argument('date',required=True)
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
            data=util.select_demanda_energia(date=args['date'],chunk_size=chunk_size)
            return data.to_dict()
        finally:
            util.close_connection()