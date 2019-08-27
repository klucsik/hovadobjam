from app import db, app
from flask import request
from app.hullinfo import *
from app.alias import *
from flask import render_template, flash, redirect, url_for
from app.forms import *
import logging

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = HullinfoKeresesForm()
    if form.validate_on_submit():
        try:
            adatlap = get_hullinfo_by_alias(form.hullinfo_alias.data)
            return redirect(url_for('hullinfo', hull_id=adatlap[0]['hull_id']))
        except Exception as e:
            logging.error('Hulladék keresés error:' + str(e))
            flash(f'a keresett hulladék nem található: {form.hullinfo_alias.data} ')
            return redirect(url_for('index'))

    form1 = HullinfoHozzaadasForm()
    if form1.validate_on_submit():
        result = create_hullinfo(name=form1.hullinfo_name.data, description=form1.hullinfo_description.data)
        flash(f"Hulladék adat felvive: {result[0]['name']} , id = {result[0]['hull_id']}")
        return redirect(url_for('index'))

    return render_template('index.html', title='Hova dobjam', form=form, form1=form1)


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
            logging.error('Hulladék keresés error:' + str(e))
            flash(f'a keresett hulladék nem található: {form1.hullinfo_alias.data}')
            return redirect(url_for('index'))

    return render_template('hullinfo.html', title='Hulladék adatlap', form1=form1, adatlap=adatlap, aliases=aliases)



# API soon




