import sqlite3

DB_file = "data.db"
db = None

def db_connect():
    global db
    connection = sqlite3.connect(DB_file)
    return db.cursor()

def db_close():
    db.commit()
    db.close()