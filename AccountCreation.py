import flask
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="lug",
    passwd="password",
    database="LUGDB"
)

