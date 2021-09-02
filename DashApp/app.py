# -*- coding: utf-8 -*-
    
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import sys
import dash_html_components as html
import pandas as pd
import requests
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from datetime import date
from dash.exceptions import PreventUpdate
from dash_html_components.H2 import H2
from apps import home, graphs, information
sys.path.append("..")

from components import sidebar
import plotly.express as px

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.GRID])

#initialiation
content = html.Div(id="page-content", children=[])

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar.sidebar,
    content,
    ], style={'columnCount' : 1}
)

ip_general = "http://18.216.83.75:80"

# --------- HOME CALLBACKS -------------

# GET DATA HOME

@app.callback([Output('contribution-home', 'figure'),
            Output('reserves-level-home', 'children')],
            [Input('home-date-input', 'date'),
            Input('home-period-input', 'value')])
def get_data_graphs(date_value, period_value):

    # Convert date
    if date_value is not None:
        date_object = date.fromisoformat(date_value)
        date_string = str(date_object.strftime('%Y-%m-%d'))

    # Connect to IP
    url = ip_general + '/data'
    params =   {"date":date_string,
    "period":period_value
    }
    r = requests.post(url = url, params = params) 
    response = r.json()

    dataframe = pd.DataFrame.from_dict(response, orient="index")

    # RESERVES LEVEL
    df_reserves = dataframe.transpose()
    reserves_level = float(df_reserves["reserves_level"][0])
    reserves_level_rounded = str(round(reserves_level, 2)) + " m3"
    
    # PIE GRAPH
    df_pie = dataframe.copy()

    df_pie = df_pie.reset_index()
    df_pie.columns = ["Type", "Value"]

    # Drop rows
    df_pie.drop(df_pie.loc[df_pie['Type']=='mean_price'].index, inplace=True)
    df_pie.drop(df_pie.loc[df_pie['Type']=='enso'].index, inplace=True)
    df_pie.drop(df_pie.loc[df_pie['Type']=='reserves_level'].index, inplace=True)

    df_pie["Value"] = pd.to_numeric(df_pie["Value"])

    figure = px.pie(df_pie, values= 'Value', names= 'Type')

    return figure, reserves_level_rounded
    
# --------- GRAPHS CALLBACKS -------------

# GET DATA GRAPHS

@app.callback([Output('mean-price-graphs', 'children'),
            Output('enso-graphs', 'children'),
            Output('reserves-level-graphs', 'children')],
            [Input('graphs-date-input', 'date'),
            Input('graphs-period-input', 'value')])
def get_data_graphs(date_value, period_value):

    # Convert date
    if date_value is not None:
        date_object = date.fromisoformat(date_value)
        date_string = str(date_object.strftime('%Y-%m-%d'))

    # Connect to IP
    url = ip_general + '/data'
    params =   {"date":date_string,
    "period":period_value
    }
    r = requests.post(url = url, params = params) 
    response = r.json()

    dataframe = pd.DataFrame.from_dict(response, orient="index")
    dataframe = dataframe.transpose()

    # MEAN PRICE
    mean_price = float(dataframe['mean_price'][0])
    mean_price_rounded = "$ " + str(round(mean_price, 2))

    # ENSO
    enso = float(dataframe["enso"][0])
    enso_rounded = str(round(enso, 2))

    # RESERVES LEVEL
    reserves_level = float(dataframe["reserves_level"][0])
    reserves_level_rounded = str(round(reserves_level, 2)) + " m3"

    return mean_price_rounded, enso_rounded, reserves_level_rounded

# GET HISTORIC GRAPHS

@app.callback([Output('demand-generation-graphs', 'figure'),
            Output('generation-type-graphs', 'figure')],
            [Input('graphs-date-input', 'date'),
            Input('graphs-period-input', 'value')])
def get_historic_graphs(date_value, period_value):

    # Convert date
    if date_value is not None:
        date_object = date.fromisoformat(date_value)
        date_string = str(date_object.strftime('%Y-%m-%d'))

    # Connect to IP
    url = ip_general + '/historic'
    params =   {"date":date_string,
    "period":period_value
    }
    r = requests.post(url = url, params = params) 
    response = r.json()

    # DEMAND AND GENERATION GRAPH

    dataframe = pd.DataFrame.from_dict(response["Demanda_Generacion"], orient="index")
    dataframe = dataframe.transpose()
    dataframe.columns = ["Demand", "Generation"]

    figure_1 = px.line(dataframe,  y=["Demand", "Generation"], line_shape="spline", render_mode="svg", title= "DEMAND AND GENERATION")
    # Horizontal Legends - Position Top Right
    figure_1.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))

    # GENERATION TYPE GRAPH

    df_total = pd.DataFrame()

    for value in response["Tipo"].values():
        df_temp = pd.DataFrame.from_dict(value["Generacion"], orient="index")
        df_temp = df_temp.transpose()
        df_total = df_total.append(df_temp, ignore_index= True)
        # print(df_temp)

    df_total = df_total.transpose()
    df_total.columns = ["COGENERATOR", "WIND", "HYDRAULIC", "SOLAR", "THERMAL"]

    figure_2 = px.line(df_total,  y=["COGENERATOR", "WIND", "HYDRAULIC", "SOLAR", "THERMAL"], line_shape="spline", render_mode="svg", title= "GENERATION TYPE")
    # Horizontal Legends - Position Top Right
    figure_2.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))

    return figure_1, figure_2

# --------- INFORMATION CALLBACKS -------------



# --------- MAIN CALLBACKS -------------

@app.callback(
Output("page-content","children"),
[Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return home.content
    if pathname == "/graphs":
        return graphs.content
    elif pathname == "/information":
        return information.content
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

# Exception - ID callbacks used in other components
app.config['suppress_callback_exceptions'] = True

if __name__=='__main__':
    app.run_server(debug=True,port=8050)