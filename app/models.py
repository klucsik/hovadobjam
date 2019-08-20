from app import db


class hullinfo(db.Model):
    __tablename__ = 'hullinfo'
    id = db.Column(db.Integer, primary_key=True)
    hull_id = db.Column(db.Integer, unique=False, nullable=False)
    name = db.Column(db.String(150), unique=False, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=True)
    version = db.Column(db.Integer, nullable=False)


class alias(db.Model):
    __tablename__ = 'alias'
    id = db.Column(db.Integer, primary_key=True)
    hull_id = db.Column(db.Integer, unique=False, nullable=False)
    name = db.Column(db.String(150), unique=True, nullable=False)


