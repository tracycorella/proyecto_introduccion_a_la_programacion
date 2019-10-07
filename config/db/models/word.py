from datetime import datetime

def init_word(db):
    class Word(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        word = db.Column(db.String(200), nullable=False)
        created = db.Column(
            db.DateTime,
            default=datetime.utcnow
        )

        def __init__(self, word):
            self.word = word

        def __repr__(self):
            return '<Word %r>' % self.id

        @staticmethod
        def add_word(word, cb):
            new_word = Word(word)
            try:
                db.session.add(new_word)
                db.session.commit()
                return cb()
            except BaseException:
                return 'There was an issue adding your word'

        @staticmethod
        def delete_word(id, cb):
            word_to_delete = Word.query.get_or_404(id)
            try:
                db.session.delete(word_to_delete)
                db.session.commit()
                return cb()
            except BaseException:
                return 'There was an issue deleting your word'

        @staticmethod
        def update(self, newdata):
            for key, value in newdata.items():
                setattr(self, key, value)

        def update_word(self, id, word, cb):
            word_to_delete = Word.query.get_or_404(id)
            self.update(word_to_delete, word)
            try:
                db.session.commit()
                return cb()
            except BaseException:
                return 'There was an issue updating your word'

        @staticmethod
        def get_played_words():
            return Word.query.order_by(Word.created).all()

    return Word
