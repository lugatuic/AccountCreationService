from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Regexp

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmpass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    prefname = StringField('Preferred Name')
    netid = StringField('netID', validators=[DataRequired(), Regexp(r'^[a-z]{2,6}\d{1,3}$', message='Not a valid netID.')])
    email = StringField('email', validators=[DataRequired(), Email()])
    uin = StringField('UIN', validators=[DataRequired(), Regexp(r'^\d{9}$',message='A UIN is 9 digits long.')])
    major = SelectField('Major', choices=[('cs', 'Computer Science'), ('ce', 'Computer Engineering')], validators=[DataRequired()])
    submit = SubmitField('Sign Up')