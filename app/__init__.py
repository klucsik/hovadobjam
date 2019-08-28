from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import logging
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

logging.basicConfig(level=logging.DEBUG)

from app import routes, models

db.create_all()
