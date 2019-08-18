from app import db

class piffs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    piffstring = db.Column(db.String(64), index=True, unique=False)
