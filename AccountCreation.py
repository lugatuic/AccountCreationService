from flask import Flask
import mysql.connector

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="lug",
    passwd="password",
    database="LUGDB"
)

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmpass = PasswordField('Confirm Password', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    prefname = StringField('Preferred Name')
    netid = StringField('netID', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    uin = IntegerField('UIN', validators=[DataRequired()])
    major = StringField('Major', validators=[DataRequired()])