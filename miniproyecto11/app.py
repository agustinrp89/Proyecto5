from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw', methods=['POST'])
def draw():
    # Aquí puedes agregar la lógica para procesar los datos recibidos del frontend
    # y realizar las operaciones de pintura en la pantalla.

    # Por ejemplo, puedes obtener las coordenadas y el color del píxel a pintar desde los datos recibidos
    x = int(request.form['x'])
    y = int(request.form['y'])
    color = request.form['color']

    # Aquí puedes agregar la lógica para pintar en la pantalla utilizando las coordenadas y el color proporcionados

    # Devuelve una respuesta al frontend
    return 'OK'

if __name__ == '__main__':
    app.run()
