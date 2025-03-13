from dash import Dash, html
import dash_bootstrap_components as dbc
import pandas as pd

from app import *


# Inicializa o app com o tema Bootstrap
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout do Sistema
app.layout = dbc.Container(children = [
    dbc.Row([
        dbc.Col(html.Div("Esquerda"), md=2, style = {'background-color': 'lightblue'}),
        dbc.Col(html.Div("Direita"), md=10, style = {'background-color': 'lightgreen'}),
    ])
], fluid = True)

# Executa o sistema
if __name__ == '__main__':
    app.run_server(debug=True)