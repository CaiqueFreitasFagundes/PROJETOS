# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='My First App with Data, Graph, and Controls'), #adicionar um texto
    html.Hr(),#adicionar uma linha horizontal
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'), #adicionar um radio button, ou seja, um botão de escolha.
    dash_table.DataTable(data=df.to_dict('records'), page_size=6), #adicionar uma tabela
    dcc.Graph(figure={}, id='controls-and-graph') #adicionar um gráfico
]

# Add controls to build the interaction
@callback( #adicionar um callback, que é uma função que é chamada quando um evento ocorre.
    Output(component_id='controls-and-graph', component_property='figure'), #adicionar um output, que é o que será atualizado quando o evento ocorrer.
    Input(component_id='controls-and-radio-item', component_property='value') #adicionar um input, que é o que será passado para a função que será chamada.
)
def update_graph(col_chosen): #adicionar uma função que atualiza o gráfico quando o usuário escolhe uma opção no radio button.
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
