from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__, static_folder='static')

api_key = 'aec5022933c801e70135b0874cc9bf39'


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


#Ao enviar o formulario ele redireciona para o /filmes passando como parametro
# o Filme digitado pelo usuario
@app.route('/busca', methods=['POST', 'GET'])
def busca():
    nome_do_filme = request.form['filme']
    return redirect(f'/filmes/{nome_do_filme}')


#Aqui é onde acessa a Api e coleta as imagens, e envia para a pagina
@app.route('/filmes/<nome_do_filme>')
def filme(nome_do_filme):
    imagens = []
    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={nome_do_filme}'
    response = requests.get(url)
    dicionario = response.json()
    if dicionario["total_results"] == 0:
        return render_template("index.html", texto_nao_encontrado="Filme não encontrado" )
    for filme in dicionario['results'][0:15]:    
        imagens.append('https://image.tmdb.org/t/p/w500' + filme["poster_path"])
    return render_template("imagens.html", imagens=imagens)


if __name__ == "__main__":
    app.run(host="localhost", debug=True)
