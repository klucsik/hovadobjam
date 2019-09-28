from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class HullinfoKeresesForm(FlaskForm):
    hullinfo_alias = StringField(label='', validators=[DataRequired()], render_kw={"placeholder": "Keress rá egy hulladékra!"})
    submit = SubmitField('Keresés')


class HullinfoHozzaadasForm(FlaskForm):
    hullinfo_name = StringField('Név', validators=[DataRequired()])
    hullinfo_description = StringField('Leírás')
    hullinfo_aliases = StringField('Más nevek')
    submit = SubmitField('Beküldés')

class HogyanForm(FlaskForm):
 comment = StringField('Te hogyan dobnád ki?',  validators=[DataRequired()])
 submit = SubmitField('Beküldés')

class LoginForm(FlaskForm):
    username = StringField('Felhasználónév', validators=[DataRequired()])
    password = PasswordField('Jelszó', validators=[DataRequired()])
    remember_me = BooleanField('Emlékezz rám')
    submit = SubmitField('Bejelentkezés')

class RegistrationForm(FlaskForm):
    username = StringField('Felhasználónév', validators=[DataRequired()])
    email = StringField('Email cím', validators=[DataRequired(), Email()])
    password = PasswordField('Jelszó', validators=[DataRequired()])
    password2 = PasswordField(
        'Jelszó mégegyszer', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Regisztrálok')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Kérlek válassz másik felhasználónevet!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Kérlek válassz másik email-címet!')