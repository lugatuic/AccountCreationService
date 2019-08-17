from flask import Flask, render_template

from db import DB
from signupform import SignupForm

app = Flask(__name__)

db = DB()

app.config.update(dict(
    SECRET_KEY="I don't see why this is necessary",
    WTF_CSRF_SECRET_KEY="I mean I don't see how this is benefitting in any way"
))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        db.create_account(form)
    return render_template('signup.html', title='Sign Up', form=form)