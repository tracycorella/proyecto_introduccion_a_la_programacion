from flask_sqlalchemy import SQLAlchemy
from config.db.models.word import init_word
from config.db.models.score import init_score
from ..paths import basedir


class DB:
    # three relative path, four slashes absolute path
    db = SQLAlchemy()
    models = {}
    connect_string = 'sqlite:///' + basedir + '/hangman.db'

    def __init__(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = self.connect_string
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db.init_app(app)
        app.app_context().push()
        self.init_models()

    def init_models(self):
        self.models['word'] = init_word(self.db)
        self.models['score'] = init_score(self.db)

    def init_db(self):
        self.db.create_all()
        self.db.session.commit()

    def add_to_db(self, entity):
        self.db.session.add(entity)
        self.db.session.commit()
