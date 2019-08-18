from app import app, db
from app.models import piffs

@app.route('/')
@app.route('/index')
def index():
    p = piffs(1,'piffnám a db-t')
    db.session.add(p)
    db.session.commit()
    return "PIFF the  World! Írtunk az adatbázisba. check /piffinfo"


@app.route('/piffinfo')
def piffinfo():
    p = piffs.query.get(1)
    return p
