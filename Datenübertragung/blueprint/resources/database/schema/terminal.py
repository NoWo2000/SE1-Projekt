from ..setup import db

terminal = 'terminal'


class TerminalSchema(db.Model):
    time = db.Column(
        db.DateTime(),
        primary_key=True,
        server_default=db.text('NOW()')
    )
    level = db.Column(
        db.String()
    )
    message = db.Column(
        db.String()
    )
