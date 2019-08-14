from flask import Flask
import mysql.connector

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="lug",
    passwd="password",
    database="LUGDB"
)
