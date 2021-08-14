# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 14:43:57 2021

@author: dusty
"""

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


scatter_graph = px.scatter(df, x="sepal_width", y="sepal_length",color="species")
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

content= html.Div([

        dcc.Graph(
            id='time-graph',
            figure=scatter_graph
        ,style=TIMELINE_GRAPH),
    ],style=MAIN_DIV_STYLE)
