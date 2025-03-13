from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Base de dados

df = pd.DataFrame({
    "Fruit": [ "Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Cria o gráfico
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Layout do Sistema
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.H2(children='''Dash: A web application framework for yout data.'''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Callbacks e funções

# Executa o sistema
if __name__ == '__main__':
    app.run_server(debug=True)