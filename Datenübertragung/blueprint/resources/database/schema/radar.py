from ..setup import db

radar = 'radar'


class RadarSchema(db.Model):
    __tablename__ = 'radar'
    __table_args__ = {'extend_existing': True}
    time = db.Column(
        db.DateTime(),
        primary_key=True,
        server_default=db.text('NOW()')
    )
    callsign = db.Column(
        db.String()
    )
    date = db.Column(
        db.DateTime()  # maybe exchange with Integer
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
