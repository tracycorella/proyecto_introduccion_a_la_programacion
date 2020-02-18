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
print(WORD)


GAME_DATA = init_game_data(WORD)


#url sin ningún parámetro
@app.route('/', methods=crud_methods)
def index():
    print('estoy en home')
    global WORD
    if request.method == 'POST':
        req = request.form
        input = req['letter']
        print(input)
        Word.add_word(input, redirect('/'))
        listaLetras = ['']
        if not utils.game_lose(GAME_DATA['tries']):
            if validations.valid_letter(input):

                for i in range(len(listaLetras)):
                    for j in range(len(WORD)):
                        if listaLetras[i] == WORD[j]:
                            if WORD[j] not in listaLetras:
                                listaLetras.append(input) #agrega una letra solo si solo si esa letra no esta ya en la lista

                if len(listaLetras) == len(WORD): #si el tamano de la lista y de la palabra son iguales, significa que ganó
                    restart()
                    return utils.game_won()

                if input not in WORD:
                    GAME_DATA['tries'] = GAME_DATA['tries'] + 1
                if GAME_DATA['tries'] == 7:
                    restart()
                    return utils.game_lose()

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
    print('estoy en restart')
    return redirect('/')

if __name__ == '__main__':
    db_instance.init_db()
    app.run(debug=True)
