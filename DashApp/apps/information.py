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
import pandas as pd
  
# append the path of the
# parent directory

import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv") 


timeline_graph = px.line(df,  y="sepal_width", color="species", line_shape="spline", render_mode="svg")
pie_graph = px.pie(df, values='species', names='species', title='Especies')  # ESTA LÍNEA CORRIGE LA FALTA DEL GRÁFICO DE PASTEL

reserves_lvl=21324
price=211324
forecast=652234

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
    "grid-column-start":"3",
    "grid-column-end": "4"
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
    "height":"95vh",
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
    "width": "45vw",
    "height":"80vh",
    #Grid Layout
    "grid-column-start":"1",
    "grid-column-end": "2"
}
SECOND_COL_STYLE = {
    "position": "relative",
    "background-color": "#fafafa",
    "top": "12vh",
    "left": "3vw",
    "width": "40vw",
    "height":"60vh",
    #Grid Layout
    "grid-column-start":"2",
    "grid-column-end": "3"
}
SUMMARY_DATA_STYLE = {
    "position": "relative",
    "background-color": "#fafafa",
    "margin": "auto",
    "height": "10vh",
    "width":"40vw",
    #Grid Layout
    "display":"grid",
    "grid-template-columns":"repeat(2,1fr)",
    "gap":"20px",
    "grid-template-rows":"1",
}
CENTRAL_ICON_STYLE = {
    "position": "relative",
    "height": "30px",
    "width":"30px",
    "display": "flex",
    "margin": "auto",
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
PIE_GRAPH = {
    "position": "relative",
    "left": 0,
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
                dcc.Graph(
                    id='pie-graph',
                    figure=pie_graph
                    ,style=PIE_GRAPH
                )
            ])
        ],
        style= FIRST_COL_STYLE,
        ),

        html.Div([
            html.P([
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quam velit, vulputate eu pharetra nec, mattis ac neque. Duis vulputate commodo lectus, ac blandit elit tincidunt id. Sed rhoncus, tortor sed eleifend tristique, tortor mauris molestie elit, et lacinia ipsum quam nec dui."
            ]),

            html.P([
                "Quisque nec mauris sit amet elit iaculis pretium sit amet quis magna. Aenean velit odio, elementum in tempus ut, vehicula eu diam. Pellentesque rhoncus aliquam mattis. Ut vulputate eros sed felis sodales nec vulputate justo hendrerit."
            ]),

            html.P([
                "Vivamus varius pretium ligula, a aliquam odio euismod sit amet. Quisque laoreet sem sit amet orci ullamcorper at ultricies metus viverra."
            ])
        ],
        style= SECOND_COL_STYLE,
        )
    ],
    style= FIRST_ROW_STYLE,
    ),
],
style=MAIN_DIV_STYLE,
)
