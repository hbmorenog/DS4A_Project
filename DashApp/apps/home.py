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
from dash_html_components import Div
import pandas as pd
  
# append the path of the
# parent directory

import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv") 


timeline_graph = px.line(df,  y="sepal_width", color="species", line_shape="spline", render_mode="svg")
pie_graph = px.pie(df, values='species', names='species', title='Especies')  # ESTA LÍNEA CORRIGE LO DEL "ESPECIES" DEL LADO DERECHO 

reserves_lvl=21324
price=211324
forecast=652234

MAIN_DIV_STYLE = {
    "position": "fixed",
    "right": 0,
    "top":"10vh",
    # "padding": "2rem 1rem",
    "width": "95%",
    "height":"90vh",
    "background-color": "#96ed98",
}

FIRST_ROW_STYLE = {
    "position": "relative",
    # "border": "1px solid #73AD21",
    "width": "100%",
    "height":"10%",
    "background-color": "#96ed98",
    #Grid Layout
    "display":"grid",
    "grid-template-columns":"repeat(3,1fr)",
    "gap":"5px",
    "grid-template-rows":"1",
}

SUMMARY_DATA_STYLE = {
    "position": "relative",
    # "border": "1px solid #73AD21",
    "background-color": "#64ba69",
    "margin": "auto",
    # "margin-left": "auto",
    # "margin-right": "auto",
    #Grid Layout
    "display":"grid",
    "grid-template-columns":"repeat(2,1fr)",
    "gap":"5px",
    "grid-template-rows":"1",
}
ICON_STYLE= {
    "position": "relative",
    "top": "10%",
    "left": "10%",
    "height": "80%",
    "width":"80%",
    "display": "flex",
    "justify-content": "center",
}
SECOND_ROW_STYLE = {
    "position": "relative",
    # "border": "3px solid #73AD21",
    "width": "100%",
    "height":"80%",
    #Grid Layout
    "display":"grid",
    "grid-template-columns":"repeat(3,1fr)",
    "gap":"20px",
    "grid-template-rows":"1",
}

TIMELINE_GRAPH={
    # "position": "absolute",
    "display:inline-block":"width:90%",
    #Grid Layout
    "grid-column-start":"1",
    "grid-column-end": "3",
    "grid-row-start":"2",
    "grid-row-end":"4"
}

PIE_GRAPH={
    # "position": "absolute",
    "display:inline-block":"width:90%",
    #Grid Layout
    "grid-column-start":"3",
    "grid-column-end": "4",
    "grid-row-start":"2",
    "grid-row-end":"4"
}

content= html.Div([ 
    html.Div([
        html.Div([
            html.Div([
                html.H3("RESERVES"),
                html.H5(str(reserves_lvl)+" m3"),
            ]),
            html.Img(src= "/assets/img/droplet-half.svg", style= ICON_STYLE),
        ],
        style= SUMMARY_DATA_STYLE,
        ),

        html.Div([
            html.Div([
                html.H3("CURRENT PRICE"),
                html.H5("$ "+str(price)),
            ]),
            html.Img(src= "/assets/img/tags.svg", style= ICON_STYLE),
        ],
        style= SUMMARY_DATA_STYLE,
        ),

        html.Div([
            html.Div([
                html.H3("FORECAST"),
                html.H5("$ "+str(forecast))
            ]),
            html.Img(src= "/assets/img/graph-up.svg", style= ICON_STYLE),
        ],
        style= SUMMARY_DATA_STYLE,
        ),

    ],
    style= FIRST_ROW_STYLE,
    ),

    html.Div([
        dcc.Graph(
            id='time-graph',
            figure=timeline_graph
            ,style=TIMELINE_GRAPH
        ),

        dcc.Graph(
            id='pie-graph',
            figure=pie_graph
            ,style=PIE_GRAPH
        )
    ],
    style= SECOND_ROW_STYLE,
    ),

],
style=MAIN_DIV_STYLE,
)
