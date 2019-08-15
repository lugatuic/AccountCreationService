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

memberSQL = "INSERT INTO Member (lastName, fullLegalName, preferredName, netid, email, UIN, major) VALUES (%s, %s, %s, %s, %s, %s, %s)"
lugdataSQL = "INSERT INTO LUGDATA (UIN, lugUserName, password) VALUES (%s, %s, %s)"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        cur = db.cursor()
        cur.execute(memberSQL, (form.lastname, form.firstname, form.prefname, form.netid, form.email, form.uin, form.major))
        cur.execute(lugdataSQL, (form.uin, form.username, form.password))
        cur.commit()
    return render_template('signup.html', title='Sign Up', form=form)