from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmpass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    prefname = StringField('Preferred Name')
    netid = StringField('netID', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    uin = IntegerField('UIN', validators=[DataRequired()])
    major = SelectField('Major', choices=[('cs', 'Computer Science'), ('ce', 'Computer Engineering')], validators=[DataRequired()])
    submit = SubmitField('Sign Up')