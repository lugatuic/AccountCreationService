from flask import Flask, render_template
import mysql.connector

from signupform import SignupForm

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="lug",
    passwd="password",
    database="LUGDB"
)

app.config.update(dict(
    SECRET_KEY="I don't see why this is necessary",
    WTF_CSRF_SECRET_KEY="I mean I don't see how this is benefitting in any way"
))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    return render_template('signup.html', title='Sign Up', form=form)