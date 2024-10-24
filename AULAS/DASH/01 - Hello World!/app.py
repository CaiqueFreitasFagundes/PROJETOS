# Importamos a biblioteca Dash e o módulo html, que será utilizado para criar o layout da aplicação
from dash import Dash, html

# Instanciamos a aplicação Dash. Dash() é uma função que cria um objeto Dash, que é a aplicação em si
app = Dash()

# app.layout é uma lista de componentes HTML que compõem o layout da aplicação. Neste caso, temos apenas um componente, que é um texto
app.layout = [html.Div(children='Hello World')]

# app.run_server() é um método que inicia o servidor da aplicação. Quando executamos o script, a aplicação é iniciada e o servidor é aberto
if __name__ == '__main__':
    app.run(debug=True)