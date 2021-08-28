# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 07:53:03 2021

@author: dusty
"""

from flask import Flask
from flask_restful import Api
from historic import Historic 
from data import Data
from forecast import Forecast
app= Flask(__name__)
api=Api(app)

api.add_resource(Historic, '/historic')
api.add_resource(Data,'/data')
api.add_resource(Forecast,'/forecast')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)