from datetime import datetime


def init_score(db):
    class Score(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(200), nullable=False)
        score = db.Column(db.Integer, nullable=False)
        created = db.Column(
            db.DateTime,
            default=datetime.utcnow
        )

        def __init__(self, name, score):
            self.name = name
            self.score = score

        def __repr__(self):
            return '<Score %r>' % self.id

    return Score
