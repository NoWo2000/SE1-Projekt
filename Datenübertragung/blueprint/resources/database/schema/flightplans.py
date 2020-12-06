from ..setup import db

FLIGHTPLANS = 'flightplans'


class FlightplansSchema(db.Model):
    __tablename__ = 'flightplans'
    __table_args__ = {'extend_existing': True}
    time = db.Column(
        db.BigInteger(),
        server_default=db.text("EXTRACT(EPOCH FROM NOW())")
    )
    callsign = db.Column(
        db.String()
    )
    ssr = db.Column(
        db.String()
    )
    rules = db.Column(
        db.String()
    )
    aircraft = db.Column(
        db.String()
    )
    wvc = db.Column(
        db.String()
    )
    equipment = db.Column(
        db.String()
    )
    origin = db.Column(
        db.String()
    )
    eobt = db.Column(
        db.BigInteger()
    )
    route = db.Column(
        db.String()
    )
    destination = db.Column(
        db.String()
    )
    eet = db.Column(
        db.Integer()
    )
    eta = db.Column(
        db.BigInteger()
    )
    status = db.Column(
        db.String()
    )
    registration = db.Column(
        db.String()
    )
    icao4444 = db.Column(
        db.String(),
        primary_key=True
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}.pop('time', None)