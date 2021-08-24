# -*- coding: utf-8 -*-
    
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import sys
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from apps import home, graphs, information
sys.path.append("..")
  
from components import top_bar
from components import sidebar

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.GRID])

#initialiation
content = html.Div(id="page-content", children=[])

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar.sidebar,
    content,
    # top_bar.topbar,
    ], style={'columnCount' : 1}
)

@app.callback(
Output("page-content","children"),
[Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return home.content
    if pathname == "/graphs": # AQUI DEBERÍA SER "/graphs"
        return graphs.content
    elif pathname == "/information": # AQUI DEBERÍA SER "/information"
        return information.content
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

if __name__=='__main__':
    app.run_server(debug=True,port=8050)