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
DATE_PICKER_STYLE={
    "color": "#1B15BF",
    "margin-top":"1vh",
    "height":"4vh",
    "width": "10vw",
    "font-size":"1em",
    #Grid Layout
    "grid-column-start":"5",
    "grid-column-end": "6"
}
FUTURE_INTERVALS_STYLE={
    "color": "#1B15BF",
    "margin-top":"1vh",
    "height":"6vh",
    "width": "10vw",
    "font-size":"1.2em",
    "-ms-transform": "translateY(-50%)",
    #Grid Layout
    "grid-column-start":"6",
    "grid-column-end": "7",
}
MODEL_DROPDOWN_STYLE={
    "color": "#1B15BF",
    "margin-top":"0.5vh",
    "height":"6vh",
    "width": "10vw",
    "font-size":"1.2em",
    "-ms-transform": "translateY(-50%)",
    #Grid Layout
    "grid-column-start":"7",
    "grid-column-end": "8",
}
PERIOD_DROPDOWN_STYLE={
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
    "width": "95vw",
    "height":"15vh",
    #Grid Layout
    "display":"grid",
    "grid-template-columns":"repeat(3,1fr)",
    "gap":"20px",
    "grid-template-rows":"1",
}
SUMMARY_DATA_STYLE = {
    "position": "relative",
    "background-color": "#fafafa",
    "margin": "auto",
    "padding": "15px",
    #Grid Layout
    "display":"grid",
    "grid-template-columns":"repeat(2,1fr)",
    "gap":"20px",
    "grid-template-rows":"1",
}
CENTRAL_ICON_STYLE= {
    "position": "relative",
    "height": "30px",
    "width":"30px",
    "display": "flex",
    "margin": "auto",
}
TEXT_STYLE= {
    "position": "relative",
    "display": "flex",
    "justify-content": "center",
    "margin": "auto",
    #Font Style
    "color": "#1B15BF",
    "font-family":"Sawasdee",
}
SECOND_ROW_STYLE = {
    "position": "relative",
    "width": "95vw",
    "height":"85vh",
    #Grid Layout
    "display":"grid",
    "grid-template-columns":"repeat(3,1fr)",
    "gap":"0px",
    "grid-template-rows":"1",
}
TIMELINE_GRAPH={
    "position": "relative",
    "left": "2vw",
    "height": "70vh",
    "width":"60vw",
    #Grid Layout
    "grid-column-start":"1",
    "grid-column-end": "3",
    "grid-row-start":"1",
    "grid-row-end":"3"
}
ERROR_DATA_STYLE = {
    "position": "relative",
    "background-color": "#fafafa",
    "left": "3vw",
    # "margin": "auto",
    "height": "15vh",
    "width":"25vw",
}
PIE_GRAPH={
    "position": "relative",
    "top": "5vh",
    "left": "3vw",
    "height": "50vh",
    "width":"25vw",
    #Grid Layout
    "grid-column-start":"3",
    "grid-column-end": "4",
}

content= html.Div([ 

    html.Div([
        html.H5("EnergyApp", style= ENERGYAPP_STYLE),

        html.H5("HOME", style= TITLE_STYLE),

        dcc.DatePickerSingle(
            id='date-picker',
            min_date_allowed=datetime.date.today() + datetime.timedelta(days=1),
            max_date_allowed=datetime.date.today().replace(year= datetime.date.today().year+ 3),
            date=datetime.date.today() + datetime.timedelta(days=1),
            placeholder= 'Date',
            style=DATE_PICKER_STYLE
        ),
        
        dcc.Input(
            id= 'future-interals',
            type= 'number',
            placeholder= 'Future intervals',
            min= 0,
            max= 100,
            step= 1,
            style=FUTURE_INTERVALS_STYLE
        ),

        dcc.Dropdown(
            id='dropdown-model',
            options=[
                {'label': 'Model1', 'value': 'Model1'},
                {'label': 'Model2', 'value': 'Model2'},
            ],
            # value='Model1',
            placeholder= 'Model',
            style=MODEL_DROPDOWN_STYLE
        ),
        
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
                html.H2("RESERVES", style= TEXT_STYLE),
                html.H3(str(reserves_lvl)+" m3", style= TEXT_STYLE),
            ]),
            html.Img(src= "/assets/img/droplet-half.svg", style= CENTRAL_ICON_STYLE),
        ],
        style= SUMMARY_DATA_STYLE,
        ),

        html.Div([
            html.Div([
                html.H2("CURRENT PRICE", style= TEXT_STYLE),
                html.H3("$ "+str(price), style= TEXT_STYLE),
            ]),
            html.Img(src= "/assets/img/tags.svg", style= CENTRAL_ICON_STYLE),
        ],
        style= SUMMARY_DATA_STYLE,
        ),

        html.Div([
            html.Div([
                html.H2("FORECAST", style= TEXT_STYLE),
                html.H3("$ "+str(forecast), style= TEXT_STYLE)
            ]),
            html.Img(src= "/assets/img/graph-up.svg", style= CENTRAL_ICON_STYLE),
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

        html.Div([
            html.Div([
                html.Div([
                    html.H2("PERCENTAGE ERROR", style= TEXT_STYLE),
                    html.H3("75%", style= TEXT_STYLE),
                ],
                style= {
                        "position": "relative",
                        "top": "4vh",
                }
                ),
            ],
            style= ERROR_DATA_STYLE,
            ),
            dcc.Graph(
                id='pie-graph',
                figure=pie_graph
                ,style=PIE_GRAPH
            )
        ])
    ],
    style= SECOND_ROW_STYLE,
    ),

],
style=MAIN_DIV_STYLE,
)
