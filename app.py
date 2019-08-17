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
    if form.is_submitted():
        cur = db.cursor()
        cur.execute(memberSQL, (form.lastname.data, form.firstname.data, form.prefname.data, form.netid.data, form.email.data, form.uin.data, form.major.data))
        cur.execute(lugdataSQL, (form.uin.data, form.username.data, form.password.data))
        db.commit()
        for x in cur:
            print(x)
    return render_template('signup.html', title='Sign Up', form=form)