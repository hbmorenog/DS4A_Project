# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 07:53:03 2021

@author: dusty
"""

from flask import Flask
from flask_restful import Api
import ast
from information import Data 
from forecast import Forecast
app= Flask(__name__)
api=Api(app)

api.add_resource(Data, '/information')
api.add_resource(Forecast,'/forecast')
if __name__ == '__main__':
    app.run(port=80)