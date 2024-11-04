from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

#Create User Form Class
class UserForm(FlaskForm):
    name_first = StringField('First Name', validators=[DataRequired()])
    name_last = StringField('Last Name', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[DataRequired()])
    password = StringField('Password')
    submit = SubmitField('Submit')

#Create Login Form Class
class LoginForm(FlaskForm):
    email = StringField('E-Mail', validators=[DataRequired()])
    password = PasswordField('Password')
    submit = SubmitField('Submit')