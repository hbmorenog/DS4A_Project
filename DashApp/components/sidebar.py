# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 22:47:28 2021

@author: dusty
"""

# Code source: https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash_html_components.Div import Div
import pandas as pd

# data source: https://www.kaggle.com/chubak/iranian-students-from-1968-to-2017
# data owner: Chubak Bidpaa
df = pd.read_csv('https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Side-Bar/iranian_students.csv')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "width": "5%",
    "height": "100vh",
    "background-color": "#ffff72",##f8f9fa
}
TITLE_BOX_STYLE= {
    "position": "relative",
    "top": 0,
    "background-color": "#c8b900",
    "height": "10vh",
}
LOGO_STYLE= {
    "position": "relative",
    "top": "10%",
    "left": "10%",
    "height": "80%",
    "width":"80%",
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
TEXT_STYLE= {
    "position": "relative",
    "display": "flex",
    "justify-content": "center",
    "margin": "auto",
}

sidebar = html.Div([
    html.Div([
        html.Img(src= "/assets/img/renewable-energy.png", style= LOGO_STYLE),
        ],
        style= TITLE_BOX_STYLE,
    ),
    html.Div([
        html.Div([
            html.Img(src= "/assets/img/house-door-fill.svg", style= ICON_STYLE),
            dbc.NavLink("HOME", href="/", active="exact", style=TEXT_STYLE),
        ],
        ),
        html.Div([
            html.Img(src= "/assets/img/file-bar-graph-fill.svg", style= ICON_STYLE),
            dbc.NavLink("GRAPHS", href="/information", active="exact", style=TEXT_STYLE),
        ],
        ),
        html.Div([
        html.Img(src= "/assets/img/newspaper.svg", style= ICON_STYLE),
        dbc.NavLink("INFO", href="/", active="exact", style=TEXT_STYLE),
        ]),
        ]),

],
style=SIDEBAR_STYLE,
)

