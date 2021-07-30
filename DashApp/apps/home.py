# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 22:58:07 2021

@author: dusty
"""

import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
  
# append the path of the
# parent directory

import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv") 


timeline_graph = px.line(df,  y="sepal_width", color="species", line_shape="spline", render_mode="svg")
pie_graph = px.pie(df, values='species', names='species', title='Especies')

reserves_lvl=21324
price=211324
forecast=652234

MAIN_DIV_STYLE = {
    "width": "100em",
    "height":"80em",
    "padding": "30px",
    "background-color": "#f8f8f8",
    "margin-top":"50px",
    #Grid Layout
    "display":"grid",
    "grid-template-columns":"repeat(3,1fr)",
    "gap":"60px",
    "grid-template-rows":"repeat(5,1fr)",
}

TIMELINE_GRAPH={
    "display:inline-block":"width:90%",
    #Grid Layout
    "grid-column-start":"1",
    "grid-column-end": "3",
    "grid-row-start":"2",
    "grid-row-end":"4"
}

PIE_GRAPH={
    "display:inline-block":"width:90%",
    #Grid Layout
    "grid-column-start":"3",
    "grid-column-end": "4",
    "grid-row-start":"2",
    "grid-row-end":"4"
}

content= html.Div([
        html.Div([
        html.H3("RESERVES"),
        html.H5(str(reserves_lvl)+" m3")
        ]),
        html.Div([
        html.H3("CURRENT PRICE"),
        html.H5("$ "+str(price))
        ]),
        html.Div([
        html.H3("FORECAST"),
        html.H5("$ "+str(forecast))
        ]),
        dcc.Graph(
            id='time-graph',
            figure=timeline_graph
        ,style=TIMELINE_GRAPH),
        dcc.Graph(
            id='pie-graph',
            figure=pie_graph
        ,style=PIE_GRAPH),
    ],style=MAIN_DIV_STYLE)
