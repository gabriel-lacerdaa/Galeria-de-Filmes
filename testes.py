import requests

api_key = 'aec5022933c801e70135b0874cc9bf39'

def nomeFilme(nome):
    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={nome}'
    response = requests.get(url)
    return response.json()

    