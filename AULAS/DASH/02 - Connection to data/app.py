# Import packages
from dash import Dash, html, dash_table
import pandas as pd

# Incorporate data. Caso voce tenha um arquivo CSV, pode carregar o arquivo localmente. Para isso utilize o seguinte comando: df = pd.read_csv('nome_do_arquivo.csv').

# Caso voce não tenha um arquivo CSV, pode carregar o arquivo de um link. Para isso utilize o seguinte comando: df = pd.read_csv('link_do_arquivo.csv').

# Nesse exemplo, estamos carregando um arquivo CSV de um link. Mas há a possibilidade de abrir arquivos de excel, json, entre outros. Basta utilizar o comando correto de cada biblioteca correta.

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash()


# App layout
# dash_table.DataTable é um componente que exibe dados em uma tabela. O argumento data é um dicionário que contém os dados que serão exibidos na tabela. O argumento page_size define o número de linhas que serão exibidas por página. Nesse caso
app.layout = [
    html.Div(children='My First App with Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=15)
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
    
# Nesse exemplo, o Dash incorpora dados de um arquivo CSV e exibe-os em uma tabela. Podemos perceber que o Dash é uma ferramenta poderosa para a visualização de dados quanto para a criação de aplicativos web. Utilizaremos o Dash para criar um aplicativo web que exibe um gráfico de barras interativo. 