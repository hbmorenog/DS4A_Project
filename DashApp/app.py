# -*- coding: utf-8 -*-
    
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import sys
import dash_html_components as html
from apps import home
sys.path.append("..")
  
from components import top_bar
from components import sidebar

app = dash.Dash(__name__)

app.layout = html.Div([
    top_bar.topbar,
    home.content,
    sidebar.sidebar
    
], style={'columnCount' : 2})

if __name__ == '__main__':
    app.run_server(debug=True,port=80)
        
