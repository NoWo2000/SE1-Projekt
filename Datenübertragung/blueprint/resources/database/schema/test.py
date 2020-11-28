from ..setup import db

test = 'test'


class TestSchema(db.Model):
    news = db.Column(db.String(), primary_key=True)
