from dash import Dash, html
import dash_bootstrap_components as dbc
import pandas as pd

from app import *


# Inicializa o app com o tema Bootstrap
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout do Sistema
app.layout = html.Div([
    dbc.Row('Cabeçalho', style={'height' : '5vh'}),
    dbc.Row([
        dbc.Col('Esquerda', md = 2, style = {'background-color': 'blue'}),
        dbc.Col('Direita', md = 10, style = {'background-color': 'red'}),       
    ], style = {'height' : '100vh'})
])

# Executa o sistema
if __name__ == '__main__':
    app.run_server(debug=True)