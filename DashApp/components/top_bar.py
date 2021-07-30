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


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# styling the sidebar
TOP_BAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "100%",
    "height" : "60px",
    "padding": "4px",
    "background-color": "#d5d5d5",
    #Grid Layout
    "display":"grid",
    "grid-template-columns":"repeat(6,1fr)",
    "gap":"10px",
    "grid-template-rows":"1"
}

TITLE_STYLE={
    "color": "#8b98f3",
    "margin":"auto",
    "font-size":"2em",
    "margin-left":"10px",
    "font-family":"Helvetica",
    #Grid Layout
    "grid-column-start":"1",
    "grid-column-end": "2"
}

DATE_PICKER_STYLE={
    "color": "#8b98f3",
    "margin":"auto",
    "width":"95%",
    #Grid Layout
    "grid-column-start":"4",
    "grid-column-end": "5"
}
MODEL_DROPDOWN_STYLE={
    "color": "#8b98f3",
    "margin":"auto",
    "height":"50px",
    "width":"95%",
    "font-size":"1.2em",
    "-ms-transform": "translateY(-50%)",
    #Grid Layout
    "grid-column-start":"5",
    "grid-column-end": "6",
}
PERIOD_DROPDOWN_STYLE={
    "color": "#8b98f3",
    "margin":"auto",
    "height":"50px",
    "width":"95%",
    "font-size":"1.2em",
    "-ms-transform": "translateY(-50%)",
    #Grid Layout
    "grid-column-start":"6",
    "grid-column-end": "7",
}


topbar = html.Div(
    [
        html.H2("NAME",style=TITLE_STYLE),
        
        dcc.DatePickerSingle(
        id='date-picker',
        min_date_allowed=datetime.date.today() + datetime.timedelta(days=1),
        max_date_allowed=datetime.date.today().replace(year= datetime.date.today().year+ 3),
        date=datetime.date.today() + datetime.timedelta(days=1),
        style=DATE_PICKER_STYLE
        ),
        
        dcc.Dropdown(
        id='dropdown-model',
        options=[
            {'label': 'Model 1', 'value': '0'},
            {'label': 'Model 2', 'value': '1'},
            {'label': 'Model 3', 'value': '2'},
            {'label': 'Model 4', 'value': '3'}
        ],
        value='0',
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
        )
        
    
    ],
    style=TOP_BAR_STYLE,
)


