from flask_wtf import FlaskForm
from wtforms import (
    PasswordField, StringField, SubmitField, SelectField, SelectMultipleField
)
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    employee_number = StringField("Employee number", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class AssignTableForm(FlaskForm):
    servers = SelectField("Servers", coerce=int)
    tables = SelectField("Tables", coerce=int)
    assign = SubmitField("Assign")


class CloseTableForm(FlaskForm):
    table = SelectField("Table", coerce=int)
    submit = SubmitField("Close")


class AddItemsForm(FlaskForm):
    menu_items = SelectMultipleField("Menu Items", coerce=int)
    order = SelectField("Order", coerce=int)
    submit = SubmitField("Add")
