import sqlite3

con = sqlite3.connect('database.db', check_same_thread=False)
cur = con.cursor()

def __init__(self, name):
    self.name = name


def inputregister(username, password):
    cur.execute(''' INSERT INTO login(email, password)
                    VALUES(?, ?) ''', (username, password))
    con.commit()

def checklogin(email, password):
    statement = f"SELECT email from login WHERE email='{email}' AND Password = '{password}';"
    cur.execute(statement)
    if not cur.fetchone():
        print("Login failed")
    else:
        return "good"

def createtable():
    cur.execute('''CREATE TABLE IF NOT EXISTS login
                    (email text, password text)''')

def printtable():
    for row in cur.execute('SELECT * FROM login'):
        print(row)

def closeconn():
    con.close()
