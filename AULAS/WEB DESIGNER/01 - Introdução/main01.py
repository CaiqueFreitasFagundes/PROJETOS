from dash import Dash, html
import dash_bootstrap_components as dbc

# Inicializa o app com o tema Bootstrap
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout do Sistema
app.layout = html.Div([
    dbc.Row([
        dbc.Col(html.Div("Primeira de três colunas"), md=4),
        dbc.Col(html.Div("Segunda de três colunas"), md=4),
        dbc.Col(html.Div("Terceira de três colunas"), md=4),
    ]),
    dbc.Row([
        dbc.Col(html.Div("Primeira de três colunas - responsivo"), width=6, lg=3),
        dbc.Col(html.Div("Segunda de três colunas - responsivo"), width=6, lg=3),
        dbc.Col(html.Div("Terceira de três colunas - responsivo"), width=6, lg=3),
    ]),
])

# Executa o sistema
if __name__ == '__main__':
    app.run_server(debug=True)