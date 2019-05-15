from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

# Create class LoginForm
class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')

# Create class SignupForm
class SignupForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Signup')

# Create class AgendaForm
# class AgendaForm(FlaskForm):
# 	agenda_name = StringField('Agenda Name', validators=[DataRequired()])
# 	password = PasswordField('Password', validators=[DataRequired()])
# 	create = SubmitField('Create')