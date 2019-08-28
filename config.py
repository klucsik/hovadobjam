import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI') or 'postgres://cwdbbcbtrtlbwo:43ab63529c97e3923d168324e3a74c94ead734bb43bf83ea11a4eb756b97278d@ec2-46-137-113-157.eu-west-1.compute.amazonaws.com:5432/d9ag7o99atdlsr'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_ECHO = True

