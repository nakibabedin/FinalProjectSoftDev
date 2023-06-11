from flask import Flask, render_template, request, redirect, session
import tweet_generator
import db

app = Flask(__name__)

## Setup secret key for session
secret_key_file = open("keys/app_secret_key.txt", "r")
secret_key = secret_key_file.read()
app.secret_key = secret_key
secret_key_file.close

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signin', methods=["GET", "POST"])
def signin():
    if(db.check_credentials(request.form['username'], request.form['password'])):
        session['username'] = request.form['username']
        session['name'] = db.get_name(request.form['username'])
        return redirect("/explore")
    if(db.check_credentials(request.form['username'], request.form['password'])):
        return render_template('login.html', error = 'login')

@app.route('/explore')
def explore():
    tweet_generator.generate_tweet("nakibabedin", "Nakib Abedin")
    tweets = tweet_generator.return_tweets()
    return render_template('index.html', data=tweets)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/newaccount', methods=["POST"])
def newaccount():

    # store the username and password
    username = request.form["username"]
    password = request.form["password"]
    name = request.form["name"]

    db.db_user_init()
    if(not (db.check_user_not_exists(username)) ):
        #if username exists, block
        return render_template('signup.html', error = 'signup')
    else:
        db.create_new_user(username, password, name)
        return redirect("/")

@app.route("/create_tweet", methods=['POST'])
def create_tweet():
    username = session['username']
    name = session['name']
    content = request.form['content']

    tweet_generator.generate_user_tweet(username, name, content)

    return redirect("/explore")


if __name__ == '__main__':
    app.debug = True
    app.run()