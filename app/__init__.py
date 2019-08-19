from flask import Flask

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://cwdbbcbtrtlbwo:43ab63529c97e3923d168324e3a74c94ead734bb43bf83ea11a4eb756b97278d@ec2-46-137-113-157.eu-west-1.compute.amazonaws.com:5432/d9ag7o99atdlsr'
db = SQLAlchemy(app)


from app import routes, models

db.create_all()