from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_excel(r'C:\Users\caiqu\Desktop\PROGRAMAÇÃO\PROJETOS\PROJETOS\ERP\MAIN\faturamento.xlsx', nrows= 4000, sheet_name='Planilha1', engine='openpyxl')

#o r'C:\Users\caiqu\Desktop\PROGRAMAÇÃO\PROJETOS\PROJETOS\ERP\MAIN\faturamento.xlsx' é o caminho do arquivo que será lido.
# nrow é o número de linhas que serão lidas, sheet_name é a aba que será lida, engine é o motor de leitura do arquivo.


# Cria o gráfico
fig = px.bar(df, x="Produto", y="Total", color="Filial", barmode="group")

# Lista do dropdown
opcoes = list(df['Filial'].unique())
opcoes.append('Todas')

# -----
# list é uma função que transforma o objeto em uma lista
# df['Filial'].unique() retorna os valores únicos da coluna Filial

# Layout do Sistema
app.layout = html.Div(children=[
    html.H1(children='Histórico de Faturamento'),
    html.H2(children='Dashboard de faturamento de produtos por filial'),
    html.Div(children='''
        Gráfico de barras com o faturamento de produtos por filial.
    '''),
    
    # Dropdown
    dcc.Dropdown(opcoes, 'Todas', id='lista-filiais'),
    html.Div(id='txt-soma-faturamento'),
    
    # dcc é uma função que cria um dropdown, o primeiro argumento é a lista de opções, o segundo é a opção padrão e o terceiro é o id do dropdown. id é um identificador único do componente.

    # Gráfico
    dcc.Graph(
        id='grafico-faturamento',
        figure=fig
    )
])



# Callbacks e funções
# atualiza_grafico é uma função que atualiza o gráfico de acordo com a filial selecionada no dropdown.

@app.callback(
    Output('grafico-faturamento', 'figure'),
    Input('lista-filiais', 'value')
)
# em Output, o primeiro argumento é o id do componente que será atualizado e o segundo é o atributo que será atualizado, note que o atributo é figure, que é o gráfico em si. Em Input, o primeiro argumento é o id do componente que será lido e o segundo é o atributo que será lido, que é value, que é o valor selecionado no dropdown.

def update_output(value):
    if value == 'Todas':
        fig = px.bar(df, x="Produto", y="Total", color="Filial", barmode="group")
        # value é o valor selecionado no dropdown, fig é o gráfico que será retornado, px.bar é a função que cria um gráfico de barras, x é a coluna que será o eixo x, y é a coluna que será o eixo y, color é a coluna que será a cor das barras e barmode é o modo de agrupamento das barras. Todas as colunas são do dataframe df, e estão referenciadas no inicio do código.
    else:
        tabela_filtrada = df.loc[df['Filial'] == value,:]
        fig = px.bar(tabela_filtrada, x="Produto", y="Total", color="Filial", barmode="group")
        # Aqui criamos a tabela_filtrada para filtrar o dataframe df de acordo com a filial selecionada no dropdown. A função loc é usada para filtrar o dataframe, o primeiro argumento é a condição de filtro e o segundo é a lista de colunas que serão retornadas. O gráfico é criado com a função px.bar, com os mesmos argumentos do gráfico anterior.
    return fig
# Atualiza o texto com o faturamento total
@app.callback(
    Output('txt-soma-faturamento', 'children'),
    Input('lista-filiais', 'value')
)

# Note que no Output, o primeiro argumento é o id do componente que será atualizado e o segundo é o atributo que será atualizado, que é children, que é o texto do componente. children é o texto que será exibido no componente, que é o faturamento total da filial selecionada no dropdown. 

def update_output(value):
    if value == 'Todas':
        faturamento_total = round(df['Total'].sum(), 2)
        # value é o valor selecionado no dropdown, faturamento_total é o faturamento total da filial selecionada, df['Total'].sum() é a soma da coluna Total do dataframe df.
    else:
        tabela_filtrada = df.loc[df['Filial'] == value,:]
        faturamento_total = round(tabela_filtrada['Total'].sum(), 2)
        # A tabela_filtrada é criada para filtrar o dataframe df de acordo com a filial selecionada no dropdown. O faturamento_total é a soma da coluna Total da tabela_filtrada.
    return f'O faturamento total é R$ {faturamento_total:.2f}'

# Executa o sistema
if __name__ == '__main__':
    app.run_server(debug=True)
    
    