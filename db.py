import mysql.connector
from wtforms.validators import ValidationError
from datetime import date

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="lug",
        passwd="password",
        database="LUGDB"
    )

def create_account(form):
    memberSQL = "INSERT INTO Member (lastName, fullLegalName, preferredName, netid, email, UIN, major, joinDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    lugdataSQL = "INSERT INTO LUGDATA (UIN, lugUserName, password) VALUES (%s, %s, %s)"

    conn = connect()
    cur = conn.cursor()
    cur.execute(memberSQL, (form.lastname.data, form.firstname.data, form.prefname.data, form.netid.data, form.email.data, form.uin.data, form.major.data, date.today()))
    cur.execute(lugdataSQL, (form.uin.data, form.username.data, form.password.data))
    conn.commit()
    conn.close()

#A validator for WTForms
class NoDupes(object):
    def __init__(self, column, table, message="Already exists in database."):
        self.column = column
        self.table = table
        self.message = message

    def __call__(self, form, field):
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT {0} FROM {1} WHERE {0} = '{2}';".format(self.column, self.table, field.data))
        if len(cur.fetchall()) > 0:
            raise ValidationError(self.message)
        conn.close()