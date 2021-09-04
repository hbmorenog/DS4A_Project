# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 22:58:07 2021

@author: dusty
"""

from dash_bootstrap_components._components.Col import Col
from dash_bootstrap_components._components.Row import Row
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import datetime
from dash_html_components import Div
from dash_html_components.Br import Br
import pandas as pd
  
# append the path of the
# parent directory

import plotly.express as px

import base64

df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv") 

# eda_path = '/home/brymo/Desktop/Projects/MinTic_Stuff/DS4A/Project/Modelos/Modelos finales/EDA_Resized_Test.jpeg'
# eda_path = '/assests/img/eda_final.jpeg'

# EDA PDF
eda_path = '/home/brymo/Desktop/Projects/MinTic_Stuff/DS4A/Project/Front/Repo Front Bryan/DS4A_Project/DashApp/assets/img/eda_final.jpeg'
eda_file_base64 = base64.b64encode(open(eda_path, 'rb').read()).decode('ascii')

# LSTM_DNN MODEL PDF

lstm_dnn_path = '/home/brymo/Desktop/Projects/MinTic_Stuff/DS4A/Project/Front/Repo Front Bryan/DS4A_Project/DashApp/assets/img/lstm_dnn_final.jpeg'
lstm_dnn_file_base64 = base64.b64encode(open(lstm_dnn_path, 'rb').read()).decode('ascii')

# reserves_lvl=21324
# price=211324
# forecast=652234

#---TOP BAR STYLE----------------------------------

TOP_BAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": "5vw",
    "width": "95vw",
    "height" : "10vh",
    "padding": "4px",
    "background-color": "#1564bf",
    #Grid Layout
    "display":"grid",
    "grid-template-columns":"repeat(8,1fr)",
    "gap":"5px",
    "grid-template-rows":"1",
}
ENERGYAPP_STYLE={
    "text-align": "left",
    "margin": "auto",
    #Font Style
    "color": "#ffffff",
    "font-size":"7vh",
    "font-family":"Karumbi",
    #Grid Layout
    "grid-column-start":"1",
    "grid-column-end": "2"
}
TITLE_STYLE={
    "text-align": "left",
    "margin": "auto",
    #Font Style
    "color": "#15B9BF",
    "font-size":"4vh",
    "font-family":"Purisa",
    #Grid Layout
    "grid-column-start":"5",
    "grid-column-end": "6"
}

#---------------------------------

MAIN_DIV_STYLE = {
    "position": "fixed",
    "right": 0,
    "top":"10vh",
    "width": "95vw",
    "height":"90vh",
    "background-color": "#bbdefb",
}
FIRST_ROW_STYLE = {
    "position": "relative",
    "width": "95vw",
    "height":"75vh", #95
    #Grid Layout
    "display":"grid",
    "grid-template-columns":"repeat(2,1fr)",
    "gap":"20px",
    "grid-template-rows":"1",
}
FIRST_COL_STYLE = {
    "position": "relative",
    "background-color": "#fafafa",
    "top": "3vh",
    "left": "3vw",
    "width": "650px",
    "height":"550px",
    #Grid Layout
    "grid-column-start":"1",
    "grid-column-end": "2"
}
SECOND_COL_STYLE = {
    "position": "relative",
    "background-color": "#fafafa",
    "top": "3vh",
    "left": "3vw",
    "width": "650px",
    "height":"550px",
    #Grid Layout
    "grid-column-start":"2",
    "grid-column-end": "3"
}
TEXT_STYLE = {
    "position": "relative",
    "display": "flex",
    "justify-content": "center",
    "margin": "auto",
    #Font Style
    "color": "#1B15BF",
    "font-family":"Sawasdee",
}
SECOND_TEXT_STYLE = {
    "position": "relative",
    "display": "flex",
    "justify-content": "center",
    "top": "-40px",
    #Font Style
    "color": "#1B15BF",
    "font-family":"Sawasdee",
}
THIRD_TEXT_STYLE = {
    "position": "relative",
    "display": "flex",
    "justify-content": "center",
    "top": "-50px",
    #Font Style
    "color": "#1B15BF",
    "font-family":"Sawasdee",
}
SECOND_ROW_STYLE = {
    "position": "relative",
    "width": "95vw",
    "height":"20vh",
    #Grid Layout
    "display":"grid",
    "grid-template-columns":"repeat(6,1fr)",
    "gap":"20px",
    "grid-template-rows":"1",
}
M1_STYLE={
    "text-align": "left",
    "margin": "auto",
    "top": "-80px",
    #Font Style
    "color": "#1B15BF",
    "font-size":"7vh",
    "font-family":"Sawasdee",
    #Grid Layout
    "grid-column-start":"1",
    "grid-column-end": "2"
}

content= html.Div([ 

    html.Div([
    html.H5("EnergyApp", style= ENERGYAPP_STYLE),

    html.H5("INFORMATION", style= TITLE_STYLE),
    ],
    style=TOP_BAR_STYLE,
    ),

    html.Div([
        html.H2("HOW IT WORKS", style= TEXT_STYLE),
    ],
    style= {
        "position": "relative",
        "top": "2vh",
    }
    ),

    html.Div([
        html.Div([
            html.Div([
                html.Div(html.Img(src="/assets/img/eda_final.jpeg", style={'height': "19218px", 'width': "550px"})),
            ],
            style={'overflowY': 'scroll', 'height': 550, 'width': 650}
            ),
        ],
        style= FIRST_COL_STYLE,
        ),

        html.Div([
            html.Div([
                html.Div(html.Img(src="/assets/img/lstm_dnn_final.jpeg", style={'height': "12451px", 'width': "550px"})),
            ],
            style={'overflowY': 'scroll', 'height': 550, 'width': 650}
            ),
        ],
        style= SECOND_COL_STYLE,
        )
    ],
    style= FIRST_ROW_STYLE,
    ),

    html.Div([
        html.H2("TEAM MEMBERS", style= SECOND_TEXT_STYLE),
    ],
    # style= SECOND_ROW_STYLE,
    ),

    html.Div([
        html.H4("ANDRÉS BOHÓRQUEZ", style= THIRD_TEXT_STYLE),
        html.H4("EDGARD RODRIGUEZ", style= THIRD_TEXT_STYLE),
        html.H4("CARLOS CONTRERAS", style= THIRD_TEXT_STYLE),
        html.H4("VICTOR LOAIZA", style= THIRD_TEXT_STYLE),
        html.H4("ANTONIO BARRIOS", style= THIRD_TEXT_STYLE),
        html.H4("BRYAN MORENO", style= THIRD_TEXT_STYLE),
    ],
    style= SECOND_ROW_STYLE,
    ),

],
style=MAIN_DIV_STYLE,
)
