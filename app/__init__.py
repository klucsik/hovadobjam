from flask import Flask, jsonify
from config import Config
from flask_sqlalchemy import SQLAlchemy
import logging
from flask_login import LoginManager
from flask_migrate import Migrate

from flask_bootstrap import Bootstrap

from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)
jwt = JWTManager(app)
CORS(app)
flask_bcrypt = Bcrypt(app)
logging.basicConfig(level=logging.DEBUG)
app.config.from_object(Config)
logging.info(f"Database url: {Config.SQLALCHEMY_DATABASE_URI}")



from app import routes, models, API_routes


