from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Regexp

from db import NoDupes

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        NoDupes('lugUserName', 'LUGDATA', message="Username is taken, please choose another.")
    ])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmpass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    prefname = StringField('Preferred Name')
    netid = StringField('netID', validators=[
        DataRequired(), 
        Regexp(r'^[a-z]{2,6}\d{1,3}$', message='Not a valid netID.'),
        NoDupes('netid', 'Member', message="An account with this netID already exists.")
    ])
    email = StringField('email', validators=[
        DataRequired(),
        Email(),
        NoDupes('email', 'Member', message="An account with this email already exists.")])
    uin = StringField('UIN', validators=[
        DataRequired(),
        Regexp(r'^\d{9}$',message='A UIN is 9 digits long.'),
        NoDupes('UIN', 'Member', message="An account with this UIN already exists.")
    ])
    major = SelectField('Major', choices=[('cs', 'Computer Science'), ('ce', 'Computer Engineering')], validators=[DataRequired()])
    submit = SubmitField('Sign Up')