import requests
from flask import Flask, request, render_template

API_KEY = 'TU_API_KEY_DE_TMDB'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    pelicula = request.form['pelicula']
    resultados = buscar_ratings_peliculas(pelicula)
    return render_template('resultados.html', resultados=resultados)

def buscar_ratings_peliculas(pelicula):
    # Realizar la solicitud a la API de TMDb
    url = f"https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': 'API_KEY',
        'query': pelicula
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Extraer los datos de cada película
    resultados = []

    for resultado in data['results']:
        # Obtener el título de la película
        titulo = resultado['title']

        # Obtener el rating de la película
        rating = resultado['vote_average']

        # Agregar los datos de la película a la lista de resultados
        resultados.append({'titulo': titulo, 'rating': rating})

    return resultados

if __name__ == '__main__':
    app.run(debug=True)
