from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import logging
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

app = Flask(__name__)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)
logging.basicConfig(level=logging.DEBUG)
app.config.from_object(Config)
from app import routes, models

