from flask import Flask, render_template, request, redirect, url_for
import random
import requests

app = Flask(__name__)

chosen_word = ""
max_attempts = 6
guessed_letters = []
attempts_left = max_attempts

@app.route('/')
def index():
    return render_template('index.html', attempts_left=attempts_left)

@app.route('/play', methods=['POST'])
def play():
    global attempts_left
    global guessed_letters

    guess = request.form['guess'].lower()

    if guess in guessed_letters:
        return redirect(url_for('index'))

    guessed_letters.append(guess)

    if guess not in chosen_word:
        attempts_left -= 1

    if attempts_left == 0:
        return render_template('index.html', word=chosen_word, message="Perdiste. La palabra era:", lost=True)

    masked_word = ''.join([char if char in guessed_letters else '_' for char in chosen_word])

    if masked_word == chosen_word:
        return render_template('index.html', word=chosen_word, message="¡Ganaste!", won=True)

    return render_template('index.html', attempts_left=attempts_left, masked_word=masked_word)

@app.route('/start', methods=['POST'])
def start():
    global chosen_word
    global guessed_letters
    global attempts_left

    chosen_word = get_random_word()
    guessed_letters = []
    attempts_left = max_attempts

    return redirect(url_for('index'))

def get_random_word():
    url = "https://random-word-api.herokuapp.com/word?number=1"
    response = requests.get(url)
    words = response.json()
    word = random.choice(words)
    return word.lower()

if __name__ == '__main__':
    app.run(debug=True)
