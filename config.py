import datetime
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_ECHO = False
    # auth
    # Configure application to store JWTs in cookies. Whenever you make
    # a request to a protected endpoint, you will need to send in the
    # access or refresh JWT via a cookie.
    JWT_TOKEN_LOCATION = ['cookies']

    # Set the cookie paths, so that you are only sending your access token
    # cookie to the access endpoints, and only sending your refresh token
    # to the refresh endpoint. Technically this is optional, but it is in
    # your best interest to not send additional cookies in the request if
    # they aren't needed.
    JWT_ACCESS_COOKIE_PATH = '/api/auth'
    JWT_REFRESH_COOKIE_PATH = '/token/refresh'

    # Disable CSRF protection for this example. In almost every case,
    # this is a bad idea. See examples/csrf_protection_with_cookies.py
    # for how safely store JWTs in cookies
    JWT_COOKIE_CSRF_PROTECT = False

    # Set the secret key to sign the JWTs with
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)



