# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 11:56:00 2021

@author: dusty
"""

from flask_restful import Resource,reqparse
from psycopg_util import Pyscopg_util
class Data(Resource):
    
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
            data=util.select_informacion(date=args['date'],chunk_size=chunk_size)
            print(data)
            return data
        finally:
            util.close_connection()