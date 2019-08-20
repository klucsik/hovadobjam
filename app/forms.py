from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class HullinfoKeresesForm(FlaskForm):
    hullinfo_alias = StringField('hullinfo_alias', validators=[DataRequired()])
    submit = SubmitField('Keresés')


class HullinfoHozzaadasForm(FlaskForm):
    hullinfo_name = StringField('hullinfo_name', validators=[DataRequired()])
    hullinfo_description = StringField('hullinfo_description', validators=[DataRequired()])
    submit = SubmitField('Beküldés')
