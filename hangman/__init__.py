import hangman.config.constants as constants
import hangman.utils as utils


# TODO remember this when we will store word
def init_game_data(word):
    return {
        'errors': [],
        'letters': [None] * len(word),
        'tries': 0,
        'word': word,
        'utils': {
            'gameOver': utils.game_over,
            'gameLose': utils.game_lose
        },
        'display': constants.DISPLAY_MSG,
    }