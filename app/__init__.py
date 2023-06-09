from flask import Flask, render_template
import tweet_generator

app = Flask(__name__)

@app.route('/')
def explore():
    tweet_generator.generate_tweet("NakibAbedin", "nakibabedin")
    tweets = tweet_generator.return_tweets()
    return render_template('index.html', data=tweets)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.debug = True
    app.run()