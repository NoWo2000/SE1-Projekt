from ..setup import db

it = 'it'


class ItSchema(db.Model):
    __tablename__ = 'it'
    __table_args__ = {'extend_existing': True}
    time = db.Column(
        db.BigInteger(),
        primary_key=True,
        server_default=db.text("EXTRACT(EPOCH FROM NOW())")
    )
    server_cpu_usage = db.Column(
        db.Integer()
    )
    server_ram_usage = db.Column(
        db.Integer()
    )
    server_login_failed = db.Column(
        db.Integer()
    )
    server_login_success = db.Column(
        db.Integer()
    )
    traffic_upload = db.Column(
        db.Integer()
    )
    traffic_download = db.Column(
        db.Integer()
    )
    news = db.Column(
        db.String()
    )
