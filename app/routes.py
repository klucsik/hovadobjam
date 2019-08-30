from app import db, app
from flask import request
from app.hullinfo import *
from app.alias import *
from flask import render_template, flash, redirect, url_for
from app.forms import *
import logging
from flask_login import login_required, current_user, logout_user, login_user
from app.models import User
from app.hova_dobjam_kimutatas import *


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = HullinfoKeresesForm()
    if form.validate_on_submit():
        try:
            adatlap = get_hullinfo_by_alias(form.hullinfo_alias.data)
            return redirect(url_for('hullinfo', hull_id=adatlap.hull_id))
        except Exception as e:
            logging.error('Hulladék keresés error:' + str(e))
            flash(f'a keresett hulladék nem található: {form.hullinfo_alias.data} ')
            return redirect(url_for('index'))

    form1 = HullinfoHozzaadasForm()
    if form1.validate_on_submit():
        result = create_hullinfo_version(name=form1.hullinfo_name.data, description=form1.hullinfo_description.data)
        flash(f"Hulladék adat felvive: {result.name} , id = {result.hull_id}")
        return redirect(url_for('index'))

    return render_template('index.html', title='Hova dobjam', form=form, form1=form1)


@app.route('/hullinfo/<hull_id>', methods=['GET', 'POST'])
@login_required
def hullinfo(hull_id):
    adatlap = get_hullinfo_versionated_by_hull_id(hull_id)
    aliases = get_aliases_from_hull_id(hull_id)
    kuka_count_list = get_kuka_count_list_readable(hull_id)

    form1 = HullinfoKeresesForm()

    if form1.validate_on_submit():
        try:
            adatlap = get_hullinfo_by_alias(form1.hullinfo_alias.data)
            return redirect(url_for('hullinfo', hull_id=adatlap.hull_id))
        except Exception as e:
            logging.error('Hulladék keresés error:' + str(e))
            flash(f'a keresett hulladék nem található: {form1.hullinfo_alias.data}')
            return redirect(url_for('index'))

    return render_template('hullinfo.html', title='Hulladék adatlap', form1=form1, adatlap=adatlap, aliases=aliases, kuka_count_list=kuka_count_list, kuka_list_len=len(kuka_count_list[0]))

@app.route('/hova_dobta/<hull_id>', methods=['GET', 'POST'])
@login_required
def hova_dobta(hull_id):
    kuka_id = request.args.get('kuka_id')
    user_id = request.args.get('user_id')
    make_hova_dobta(hull_id=hull_id, user_id=user_id, kuka_id=kuka_id)
    flash(f"köszi hogy kidobtad a {hull_id} IDvel rendelkező szemetet a {kuka_id} IDjű kukába!")
    #TODO: trystruktúra az error handlinghoz

    return redirect(url_for('index'))



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    # noinspection PyArgumentList
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)