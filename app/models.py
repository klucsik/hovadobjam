from app import db
from flask_login import UserMixin
from app import login
from werkzeug.security import generate_password_hash, check_password_hash

class hullinfo(db.Model):
    __tablename__ = 'hullinfo'
    id = db.Column(db.Integer, primary_key=True)
    hull_id = db.Column(db.Integer, unique=False, nullable=False)
    name = db.Column(db.String(150), unique=False, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=True)
    version = db.Column(db.Integer, nullable=False)


class aliasTable(db.Model):
    __tablename__ = 'alias'
    id = db.Column(db.Integer, primary_key=True)
    hull_id = db.Column(db.Integer, unique=False, nullable=False)
    name = db.Column(db.String(150), unique=True, nullable=False)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
# TODO: db connection with hova dobta

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# TODO: create hova dobta

