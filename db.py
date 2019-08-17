import mysql.connector

class DB:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="lug",
            passwd="password",
            database="LUGDB"
        )

    def create_account(self, form):
        memberSQL = "INSERT INTO Member (lastName, fullLegalName, preferredName, netid, email, UIN, major) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        lugdataSQL = "INSERT INTO LUGDATA (UIN, lugUserName, password) VALUES (%s, %s, %s)"

        cur = self.conn.cursor()
        cur.execute(memberSQL, (form.lastname.data, form.firstname.data, form.prefname.data, form.netid.data, form.email.data, form.uin.data, form.major.data))
        cur.execute(lugdataSQL, (form.uin.data, form.username.data, form.password.data))
        self.conn.commit()
        
        for x in cur:
            print(x)
    