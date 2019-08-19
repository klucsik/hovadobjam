from app import db

class piffs(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    piff = db.Column(db.String(80), unique=False, nullable=False)


    def __repr__(self):
        return '<PIFF: %r>' % self.piff

# db.create_all()-al lehet felküdleni a sémánkat