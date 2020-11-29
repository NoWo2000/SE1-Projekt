from ..setup import db

RADAR = 'radar'

class RadarSchema(db.Model):
    __tablename__ = 'radar'
    __table_args__ = {'extend_existing': True}
    id = db.Column(
        db.Integer(),
        primary_key=True
    )
    time = db.Column(
        db.BigInteger(),
        server_default=db.text("EXTRACT(EPOCH FROM NOW())")
    )
    callsign = db.Column(
        db.String()
    )
    date = db.Column(
        db.BigInteger()
    )
    lat = db.Column(
        db.Float()
    )
    lon = db.Column(
        db.Float()
    )
    alt = db.Column(
        db.Integer()
    )
