from app import app, db
from app.models import piffs

@app.route('/')
@app.route('/index')
def index():
    p = piffs(piff= 'PIFF the DataBase!')
    db.session.add(p)
    db.session.commit()
    return "PIFF the  World! Írtunk az adatbázisba. check /piffinfo"


@app.route('/piffinfo')
def piffinfo():
    p = piffs.query.all()
    print(p)
    return p[1].piff

@app.route('/createdb')
def createdb():
    db.create_all()
    return 'db created'