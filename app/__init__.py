from flask import Flask, render_template, request, redirect
import tweet_generator

app = Flask(__name__)

@app.route('/')
def explore():
    tweet_generator.generate_tweet("nakibabedin", "Nakib Abedin")
    tweets = tweet_generator.return_tweets()
    return render_template('index.html', data=tweets)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route("/create_tweet", methods=['POST'])
def create_tweet():
    username = request.form['username']
    name = request.form['name']
    content = request.form['content']

    tweet_generator.generate_user_tweet(username, name, content)

    return redirect("/")


if __name__ == '__main__':
    app.debug = True
    app.run()