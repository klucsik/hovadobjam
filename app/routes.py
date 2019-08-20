from app import db, app
from flask import request
from app.hullinfo import *
from flask import render_template, flash, redirect
from app.forms import *


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='Kezdő oldal')


@app.route('/hulladek_keresese', methods=['GET', 'POST'])
def hulladek_keresese():
    form = HullinfoKeresesForm()
    if form.validate_on_submit():
        flash('Hulladék adat keresése: {}'.format(
            form.hullinfo_alias.data))
        return redirect('/hulladek_keresese')
    return render_template('hulladek_keresese.html', title='Hulladék keresése', form=form)


@app.route('/hulladek_bekuldese', methods=['GET', 'POST'])
def hulladek_bekuldese():
    form = HullinfoHozzaadasForm()
    if form.validate_on_submit():
        result = create_hullinfo(name=form.hullinfo_name.data, description=form.hullinfo_description.data)
        flash('Hulladék adat felvive: {} , id = {}'.format(
             result.name, result.hull_id))
        return redirect('/index')

    return render_template('hulladek_bekuldese.html', title='Hulladék adatlap', form=form)







# API

@app.route('/api/createdb')
def createdb():
    db.create_all()
    return 'db created'

@app.route('/api/hullinfo', methods=['GET', 'POST', 'PUT'])
def api_hullinfo():
    if request.method == 'POST':
        post_hullinfo_data = request.json
        print(post_hullinfo_data)
        result = create_hullinfo(post_hullinfo_data['name'], hull_id=post_hullinfo_data['hull_id'])

    return 'created: "' + str(result.name) + '" with hull_id = ' + str(result.hull_id) + ', version = ' + str(result.version) + ' and row id of ' + str(result.id)

