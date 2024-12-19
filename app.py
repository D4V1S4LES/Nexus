from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Rota para exibir o formulário e inserir dados
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# Rota para consulta dos dados na tabela 'teste'
@app.route('/game', methods=['GET'])
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)
