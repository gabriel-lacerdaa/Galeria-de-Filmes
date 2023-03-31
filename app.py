from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__, static_folder='static')

api_key = 'c99099d0'


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/busca', methods=['POST', 'GET'])
def busca():
    nome_do_filme = request.form['filme']
    return redirect(f'/filmes/{nome_do_filme}')


@app.route('/filmes/<nome_do_filme>')
def filme(nome_do_filme):
    imagens = []
    url = f'https://www.omdbapi.com/?apikey={api_key}&s={nome_do_filme}&type=movie'
    response = requests.get(url)
    dicionario = response.json()
    if 'Error' in dicionario.keys():
        return '<h1>Filme não encontrado</h1>'
    for filme in dicionario['Search'][0:10]:    
        imagens.append(filme["Poster"])
    return render_template("index.html", imagens=imagens)


if __name__ == "__main__":
    app.run(debug=True)
