from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class FEMAWebForm(FlaskForm):
    state = StringField('Choose a State', validators=[DataRequired()])
    submit = SubmitField('Select')
