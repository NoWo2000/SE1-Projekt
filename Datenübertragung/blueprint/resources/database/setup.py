from flask_sqlalchemy import SQLAlchemy
from ..server import app
from ..utils import config

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres+psycopg2://" \
     + config["DATABASE"]["user"] + ":" + config["DATABASE"]["password"] + "@" \
     + config["DATABASE"]["host"] + ":" + config["DATABASE"]["port"] \
     + "/" + config["DATABASE"]["database_name"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

db = SQLAlchemy(app)
