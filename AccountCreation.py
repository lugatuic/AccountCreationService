from flask import Flask
import mysql.connector

from SignupForm import SignupForm

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="lug",
    passwd="password",
    database="LUGDB"
)