from ..setup import db
from sqlalchemy.dialects.postgresql import ARRAY
event = "event"


class EventSchema(db.Model):
    __tablename__ = 'event'
    __table_args__ = {'extend_existing': True}
    id = db.Column(
        db.Integer(),
        primary_key=True
    )
    time = db.Column(
        db.BigInteger(),
        server_default=db.text("EXTRACT(EPOCH FROM NOW())")
    )
    affectedSystems = db.Column(
        ARRAY(db.String())
    )
    suspectedAttackType = db.Column(
        db.String()
    )
    probability = db.Column(
        db.Integer()
    )
    automaticReaction = db.Column(
        ARRAY(db.String())
    )
    checklist = db.Column(
        ARRAY(db.String())
    )
