import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="lug",
        passwd="password",
        database="LUGDB"
    )

def create_account(form):
    memberSQL = "INSERT INTO Member (lastName, fullLegalName, preferredName, netid, email, UIN, major) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    lugdataSQL = "INSERT INTO LUGDATA (UIN, lugUserName, password) VALUES (%s, %s, %s)"

    conn = connect()
    cur = conn.cursor()
    cur.execute(memberSQL, (form.lastname.data, form.firstname.data, form.prefname.data, form.netid.data, form.email.data, form.uin.data, form.major.data))
    cur.execute(lugdataSQL, (form.uin.data, form.username.data, form.password.data))
    conn.commit()
    
    for x in cur:
        print(x)

#A validator for WTForms
class no_dupes(object):
    def __init__(self, column, message):
        self.column = column
        self.message = message

    def __call__(self, form, field):
        conn = connect()
        cur = conn.cursor()