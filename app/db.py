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

def tweet_table_init():
    '''
    Tweet Components:
    1) Profile Picture
    2) Username
    3) Name
    4) Tweet content
    4) Likes
    '''
    c =  db_connect()
    c.execute("CREATE TABLE IF NOT EXISTS stories (pfp text, username text, name text, content text, likes int)")
    db_close()


