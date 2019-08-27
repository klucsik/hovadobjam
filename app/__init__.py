from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
logging.basicConfig(level=logging.DEBUG)

from app import routes, models

db.create_all()
