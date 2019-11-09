import datetime
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)
    AUTH0_DOMAIN = 'dev-d7jnerg6.eu.auth0.com'
    API_AUDIENCE = 'https://hovadobjam-test.herokuapp.com/api/auth0'
    ALGORITHMS = ["RS256"]



