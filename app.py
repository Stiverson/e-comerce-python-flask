# Importação da biblioteca

from flask import Flask

app = Flask(__name__)

# definição da rota raiz ( página inicial) e a função que será executada ao fazer a requisição.

@app.route('/')
def hello_first_world():
    return 'Flask and python project e demos inicio a mais um projeto'

if __name__ == "__main__":
    app.run(debug=True)