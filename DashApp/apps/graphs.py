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
PERIOD_DROPDOWN_STYLE = {
    "color": "#1B15BF",
    "margin-top":"0.5vh",
    "height":"6vh",
    "width": "10vw",
    "font-size":"1.2em",
    "-ms-transform": "translateY(-50%)",
    #Grid Layout
    "grid-column-start":"8",
    "grid-column-end": "9",
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
    "width": "100%",
    "height":"40vh",
    #Grid Layout
    "display":"grid",
    "grid-template-columns":"repeat(2,1fr)",
    "gap":"20px",
    "grid-template-rows":"1",
}
FIRST_COL_STYLE = {
    "position": "relative",
    "background-color": "#fafafa",
    "margin": "auto",
    #Grid Layout
    "grid-column-start":"1",
    "grid-column-end": "2"
}
SECOND_COL_STYLE = {
    "position": "relative",
    "background-color": "#fafafa",
    "margin": "auto",
    #Grid Layout
    "grid-column-start":"2",
    "grid-column-end": "3"
}
SUMMARY_DATA_STYLE = {
    "position": "relative",
    "background-color": "#fafafa",
    "top": "1vh",
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
    "top": "0vh",
    "left": 0,
    "height": "35vh",
    "width":"40vw",
}
SECOND_ROW_STYLE = {
    "position": "relative",
    "width": "95vw",
    "height":"60vh",
}
TIMELINE_GRAPH ={
    "position": "relative",
    "top": "0vh",
    "left": "5vw",
    "height": "45vh",
    "width":"85vw",
}

content= html.Div([ 

    html.Div([
    html.H5("EnergyApp", style= ENERGYAPP_STYLE),

    html.H5("GRAPHS", style= TITLE_STYLE),

    dcc.Dropdown(
        id='dropdown-period',
        options=[
            {'label': 'Daily', 'value': 'Daily'},
            {'label': 'Monthly', 'value': 'Monthly'},
            {'label': 'Yearly', 'value': 'Yearly'},
        ],
        # value='Daily',
        placeholder= 'Period',
        style=PERIOD_DROPDOWN_STYLE
    )],
    style=TOP_BAR_STYLE,
    ),

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H2("MEAN PRICE", style= TEXT_STYLE),
                    html.H5("Mean price  in the current month", style= TEXT_STYLE),
                ]),
                html.H2("$ 1.340", style= TEXT_STYLE),
            ],
            style= SUMMARY_DATA_STYLE,
            ),

            html.Div([
                html.Div([
                    html.H2("ENSO", style= TEXT_STYLE),
                    html.H5("El Niño–Southern Oscillation (ENSO) ", style= TEXT_STYLE),
                ]),
                html.H2("0.5", style= TEXT_STYLE),
            ],
            style= SUMMARY_DATA_STYLE,
            ),

            html.Div([
                html.Div([
                    html.H2("RESERVES LEVEL", style= TEXT_STYLE),
                    html.H5("Total amount of water stored in reservoirs", style= TEXT_STYLE),
                ]),
                html.H2("5'100.234 m3", style= TEXT_STYLE)
            ],
            style= SUMMARY_DATA_STYLE,
            ),
        ],
        style= FIRST_COL_STYLE,
        ),

        html.Div([
            dcc.Graph(
                id='pie-graph',
                figure=pie_graph
                ,style=PIE_GRAPH
            )
        ],
        style= SECOND_COL_STYLE,
        )
    ],
    style= FIRST_ROW_STYLE,
    ),

    html.Div([
        dcc.Graph(
            id='time-graph',
            figure=timeline_graph
            ,style=TIMELINE_GRAPH
        ),
    ],
    style= SECOND_ROW_STYLE,
    ),

],
style=MAIN_DIV_STYLE,
)
