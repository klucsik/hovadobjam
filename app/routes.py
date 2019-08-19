from app import db, app
from flask import request
from app.hullinfo import *

@app.route('/')
@app.route('/index')
def index():

    return "Hello there. Jelenleg a hullinfo api készülődik. check dat"


@app.route('/createdb')
def createdb():
    db.create_all()
    return 'db created'

@app.route('/hullinfo', methods=['GET', 'POST', 'PUT'])
def hullinfo():
    if request.method == 'POST':
        post_hullinfo_data = request.json
        print(post_hullinfo_data)
        result = create_hullinfo(post_hullinfo_data['name'], hull_id=post_hullinfo_data['hull_id'])

    return 'created: "' + str(result.name) + '" with hull_id = ' + str(result.hull_id) + ', version = ' + str(result.version) + ' and row id of ' + str(result.id)
