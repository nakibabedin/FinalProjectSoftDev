import sqlite3

DB_file = "data.db"
db = None

def db_connect():
    global db
    db = sqlite3.connect(DB_file)
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
    c.execute("CREATE TABLE IF NOT EXISTS tweets (pfp text, username text, name text, content int, likes int)")
    db_close()

def create_tweet(pfp, username, name, content, likes):
    c = db_connect()
    c.execute('INSERT INTO tweets VALUES (?, ?, ?, ?, ?)', (pfp, username , name , content , likes))
    db_close()

def print_tweets():
    c = db_connect()
    c.execute("SELECT * FROM tweets")
    print(c.fetchall())
    db_close()





