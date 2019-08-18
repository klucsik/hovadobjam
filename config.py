import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = 'https://data.heroku.com/datastores/526482ca-b0c2-4bfe-b91d-90979a4f3821'
    SQLALCHEMY_TRACK_MODIFICATIONS = False