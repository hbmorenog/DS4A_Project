# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 18:09:12 2021

@author: dusty
"""

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import datetime

from dash_html_components.H5 import H5


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# Styling the TopBar
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
    "grid-template-columns":"repeat(7,1fr)",
    "gap":"5px",
    "grid-template-rows":"1",
}
ENERGYAPP_STYLE={
    "top": 0,
    "text-align": "left",
    "color": "#31893d",
    "font-size":"2vh",
    "font-family":"Helvetica",
    #Grid Layout
    "grid-column-start":"1",
    "grid-column-end": "2"
}
TITLE_STYLE={
    "top": 0,
    "text-align": "left",
    "color": "#64ba69",
    "font-size":"2vh",
    "font-family":"Helvetica",
    #Grid Layout
    "grid-column-start":"3",
    "grid-column-end": "4"
}
DATE_PICKER_STYLE={
    "color": "#31893d",
    "margin":"auto",
    "width":"100%",
    "font-size":"1.2em",
    #Grid Layout
    "grid-column-start":"5",
    "grid-column-end": "6"
}
MODEL_DROPDOWN_STYLE={
    "color": "#31893d",
    "margin":"auto",
    "width":"100%",
    "font-size":"1.2em",
    "-ms-transform": "translateY(-50%)",
    #Grid Layout
    "grid-column-start":"6",
    "grid-column-end": "7",
}
PERIOD_DROPDOWN_STYLE={
    "color": "#31893d",
    "margin":"auto",
    "width":"100%",
    "font-size":"1.2em",
    "-ms-transform": "translateY(-50%)",
    #Grid Layout
    "grid-column-start":"7",
    "grid-column-end": "8",
}


topbar = html.Div([
    html.H5("EnergyApp", style= ENERGYAPP_STYLE),

    html.H5("HOME", style= TITLE_STYLE),

    dcc.DatePickerSingle(
        id='date-picker',
        min_date_allowed=datetime.date.today() + datetime.timedelta(days=1),
        max_date_allowed=datetime.date.today().replace(year= datetime.date.today().year+ 3),
        date=datetime.date.today() + datetime.timedelta(days=1),
        style=DATE_PICKER_STYLE
    ),
    
    dcc.Input(
        id= 'future-interals',
        type= 'number',
        placeholder= 'Future intervals',
        min= 0,
        max= 100,
        step= 1,
        style=MODEL_DROPDOWN_STYLE
    ),
    
    dcc.Dropdown(
        id='dropdown-period',
        options=[
            {'label': 'Daily', 'value': 'Daily'},
            {'label': 'Monthly', 'value': 'Monthly'},
            {'label': 'Yearly', 'value': 'Yearly'},
        ],
        value='Daily',
        style=PERIOD_DROPDOWN_STYLE
    )],
    style=TOP_BAR_STYLE,
)


