from flask import Flask, make_response, redirect, request, jsonify, render_template
from flask_cors import CORS
from hangman import init_game_data
import hangman.config.constants as constants
import hangman.utils as utils
import hangman.validations as validations
from config.db import DB
from config.api import WordApi

app = Flask(__name__)  # referencing current file
CORS(app)

db_instance = DB(app)

crud_methods = ['GET', 'POST']
Word = db_instance.models['word']
WORD = WordApi.get_word()

#Word.add_word(word_here, redirect('/')) add word to db

GAME_DATA = init_game_data(WORD)


@app.route('/', methods=crud_methods)
def index():
    global WORD
    if request.method == 'POST':
        req = request.form
        # TODO handle game logic functionality different
        # handle different scenarios
        # handle errors
        # handle tries
        input = req['letter']
        print(input)
        return redirect('/')
    else:
        GAME_DATA['words'] = Word.get_played_words()
        return render_template(
            'index.html',
            instructions=constants.INSTRUCTIONS,
            game=GAME_DATA)


@app.route('/restart', methods=['GET'])
def restart():
    # TODO make restart functionality
    return redirect('/')

if __name__ == '__main__':
    db_instance.init_db()
    app.run(debug=True)
