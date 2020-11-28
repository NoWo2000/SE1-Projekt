from ..setup import db

terminal = 'terminal'


class TerminalSchema(db.Model):
    __tablename__ = 'terminal'
    __table_args__ = {'extend_existing': True}
    id = db.Column(
        db.Integer(),
        primary_key=True
    )
    time = db.Column(
        db.BigInteger(),
        server_default=db.text("EXTRACT(EPOCH FROM NOW())")
    )
    level = db.Column(
        db.String()
    )
    message = db.Column(
        db.String()
    )
