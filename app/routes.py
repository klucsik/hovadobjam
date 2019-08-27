from app import db, app
from flask import request
from app.hullinfo import *
from app.alias import *
from flask import render_template, flash, redirect, url_for
from app.forms import *
import logging as logger

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = HullinfoKeresesForm()
    if form.validate_on_submit():
        try:
            adatlap = get_hullinfo_by_alias(form.hullinfo_alias.data)
            return redirect(url_for('hullinfo', hull_id=adatlap[0]['hull_id']))
        except Exception as e:
            logger.error('Hulladék keresés error:' + str(e))
            flash(f'a keresett hulladék nem található: {form.hullinfo_alias.data} ')
            return redirect(url_for('index'))

    form1 = HullinfoHozzaadasForm()
    if form1.validate_on_submit():
        result = create_hullinfo(name=form1.hullinfo_name.data, description=form1.hullinfo_description.data)
        flash(f"Hulladék adat felvive: {result[0]['name']} , id = {result[0]['hull_id']}")
        return redirect(url_for('index'))

    return render_template('index.html', title='Hova dobjam', form=form, form1=form1)


@app.route('/hulladek_keresese', methods=['GET', 'POST'])
def hulladek_keresese():
    form = HullinfoKeresesForm()
    if form.validate_on_submit():
        try:
            adatlap = get_hullinfo_by_alias(form.hullinfo_alias.data)
            return redirect(url_for('hullinfo', hull_id=adatlap[0]['hull_id']))
        except Exception as e:
            logger.error('Hulladék keresés error:' + str(e))
            flash(f'a keresett hulladék nem található: {form.hullinfo_alias.data}')
            return redirect(url_for('index'))
    return render_template('hulladek_keresese.html', title='Hulladék keresése', form=form)


@app.route('/hulladek_bekuldese', methods=['GET', 'POST'])
def hulladek_bekuldese():
    form = HullinfoHozzaadasForm()
    if form.validate_on_submit():
        result = create_hullinfo(name=form.hullinfo_name.data, description=form.hullinfo_description.data)
        flash(f"Hulladék adat felvive: {result[0]['name']} , id = {result[0]['hull_id']}")
        return redirect(url_for('index'))

    return render_template('hulladek_bekuldese.html', title='Hulladék beküldés', form=form)


@app.route('/hullinfo/<hull_id>', methods=['GET', 'POST'])
def hullinfo(hull_id):
    adatlap = get_hullinfo_by_hull_id(hull_id)
    aliases = get_aliases_from_hull_id(hull_id)

    form1 = HullinfoKeresesForm()

    if form1.validate_on_submit():
        try:
            adatlap = get_hullinfo_by_alias(form1.hullinfo_alias.data)
            return redirect(url_for('hullinfo', hull_id=adatlap[0]['hull_id']))
        except Exception as e:
            logger.error('Hulladék keresés error:' + str(e))
            flash(f'a keresett hulladék nem található: {form1.hullinfo_alias.data}')
            return redirect(url_for('index'))


    form2 = HullinfoHozzaadasForm()
    if form2.validate_on_submit():
        result = create_hullinfo(name=form2.hullinfo_name.data, description=form2.hullinfo_description.data)
        flash(f"Hulladék adat felvive: {result[0]['name']} , id = {result[0]['hull_id']}")
        return redirect(url_for('index'))
    return render_template('hullinfo.html', title='Hulladék adatlap', form1=form1, form2=form2, adatlap=adatlap, aliases=aliases)



# API soon
'''
@app.route('/api/createdb')
def createdb():
    db.create_all()
    return 'db created'

@app.route('/api/hullinfo', methods=['GET', 'POST'])
def api_hullinfo():
    if request.method == 'POST':
        post_hullinfo_data = request.json
        print(post_hullinfo_data)
        result = create_hullinfo(post_hullinfo_data['name'], hull_id=post_hullinfo_data['hull_id'])

        return 'created: "' + str(result[0]['name']) + '" with hull_id = ' + str(
            result[0]['hull_id']) + ', version = ' + str(result[0]['version']) + ' and row id of ' + str(
            result[0]['id'])

    else:
        req_hull_id = request.args.get('hull_id')
        req_version = request.args.get('version')
        result = get_hullinfo_by_hull_id(req_hull_id, req_version)

        return 'searched: "' + str(result[0]['name']) + '" with hull_id = ' + str(
            result[0]['hull_id']) + ', version = ' + str(result[0]['version']) + ' and row id of ' + str(
            result[0]['id'])
'''



