from app import db
from flask_login import UserMixin
from app import login
from werkzeug.security import generate_password_hash, check_password_hash


class HullInfoVersionated(db.Model):
    __tablename__ = 'hull_info_versionated'
    id = db.Column(db.Integer, primary_key=True)
    hull_id = db.Column(db.Integer, unique=False, nullable=False, index=True)
    name = db.Column(db.String(150), unique=False, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=True)
    version = db.Column(db.Integer, nullable=False)


class HullInfo(db.Model):
    __tablename__ = 'hullinfo'
    hull_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=True)
    version = db.Column(db.Integer, nullable=False)


class AliasTable(db.Model):
    __tablename__ = 'alias'
    id = db.Column(db.Integer, primary_key=True)
    hull_id = db.Column(db.Integer, unique=False, nullable=False)
    name = db.Column(db.String(150), unique=True, nullable=False, index=True)


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


class Kuka(db.Model):
    __tablename__ = 'kuka'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), index=True, unique=True, nullable=False)


class UserHovaDobta(db.Model):
    __tablename__ = 'user_hova_dobta'
    id = db.Column(db.Integer, primary_key=True)
    hull_id = db.Column(db.Integer, db.ForeignKey('hullinfo.hull_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    kuka_id = db.Column(db.Integer, db.ForeignKey('kuka.id'))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
