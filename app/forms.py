from flask_wtf import FlaskForm
from wtforms import (
    PasswordField, StringField, SubmitField
)
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    employee_number = StringField('Employee number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
