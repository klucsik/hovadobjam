from app.alias import *
from flask import render_template, flash, redirect, url_for, request, g
from app.forms import *
from flask_login import login_required, current_user, logout_user, login_user
from app.hova_dobjam_kimutatas import *
from app.hogyan_dobjam import *
import time


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = HullinfoKeresesForm()

    if form.validate_on_submit():

        alias = form.hullinfo_alias.data
        hull_list = get_hullinfo_list_by_alias(alias)
        if len(hull_list) > 0:
            return render_template('index.html', title='Hova dobjam', form=form, hull_list=hull_list)
        else:
            flash(f'a  "{form.hullinfo_alias.data}" eddig nem volt a rendszerben, de te most beviheted! ')
            return redirect(url_for('letrehozas', kereses=form.hullinfo_alias.data))

    return render_template('index.html', title='Hova dobjam', form=form)


@app.route('/letrehozas', methods=['GET', 'POST'])
@login_required
def letrehozas():

    form = HullinfoHozzaadasForm()

    if form.validate_on_submit():
        result = create_hullinfo(name=form.hullinfo_name.data)
        if len(form.hullinfo_alias_1.data) > 0:
            make_alias(alias=form.hullinfo_alias_1.data, hull_id=result.hull_id)
        if len(form.hullinfo_alias_2.data) > 0:
            make_alias(alias=form.hullinfo_alias_2.data, hull_id=result.hull_id)
        if len(form.hullinfo_alias_3.data) > 0:
            make_alias(alias=form.hullinfo_alias_3.data, hull_id=result.hull_id)
        #  if form.hullinfo_pic.data:
        #    file_url=1
            #  todo : http://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/

        #    logging.debug(f"uploaded photo: {file_url}")
        flash(f"Hulladék adat felvive: {result.name} , id = {result.hull_id}! hova dobnád?")
        return redirect(url_for('hullinfo', hull_id=result.hull_id))
    elif request.method == 'GET':
       form.hullinfo_name.data = request.args.get('kereses')
    return render_template('letrehozas.html', title='Hova dobjam', form=form)


@app.route('/hullinfo/<hull_id>', methods=['GET', 'POST'])
@login_required
def hullinfo(hull_id):
    adatlap = get_hullinfo_by_hull_id(hull_id)
    aliases = get_aliases_from_hull_id(hull_id)
    kuka_count_list = get_kuka_count_list(hull_id)
    hogyan_dobjam_list = get_hogyan_dobjam(hull_id)
    hogyan_form = HogyanForm()

    form = HullinfoKeresesForm()
    if form.validate_on_submit():
        try:
            adatlap = get_hullinfo_by_alias(form.hullinfo_alias.data)
            return redirect(url_for('hullinfo', hull_id=adatlap.hull_id))
        except Exception as e:
            logging.error('Hulladék keresés error:' + str(e))
            flash(f'a  "{form.hullinfo_alias.data}" eddig nem volt a rendszerben, kérlek vidd be! ')
            return redirect(url_for('letrehozas', kereses=form.hullinfo_alias.data))

    if hogyan_form.validate_on_submit():
        make_hogyan_dobjam(current_user.id, int(hull_id), hogyan_form.comment.data)
        return redirect(url_for('hullinfo', hull_id=hull_id))

    return render_template('hullinfo.html', title='Hulladék adatlap', form=form, hogyan_form=hogyan_form, adatlap=adatlap, aliases=aliases, kuka_count_list=kuka_count_list, hogyan_dobjam_list=hogyan_dobjam_list)


@app.route('/hova_dobta/<hull_id>', methods=['GET', 'POST'])
@login_required
def hova_dobta(hull_id):
    kuka_id = request.args.get('kuka_id')
    user_id = request.args.get('user_id')
    make_hova_dobta(hull_id=hull_id, user_id=user_id, kuka_id=kuka_id)
    flash(f'köszi hogy kidobtad a "{HullInfo.query.filter_by(hull_id=hull_id).first().name}"  szemetet a "{Kuka.query.filter_by(id=kuka_id).first().name}" kukába!')
    #TODO: trystruktúra az error handlinghoz

    return redirect(url_for('index'))


@app.route('/hogyan_dobjam', methods=['GET', 'POST'])
@login_required
def hogyan_dobjam_score():
    # todo: ezt ajaxxal meghívni
    hull_id = int(request.args.get('hull_id'))
    comment_id = int(request.args.get('comment_id'))
    user_id = int(request.args.get('user_id'))
    increment = int(request.args.get('increment'))
    score_hogyan_dobjam(comment_id, user_id, increment)
    return redirect(url_for('hullinfo', hull_id=hull_id))

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


@app.before_request
def before_request():
    g.request_start_time = time.time()
    g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)
