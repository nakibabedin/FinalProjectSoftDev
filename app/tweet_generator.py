from apis import duck, riddle, uselessfacts
import db
import random
'''
Tweet Components:
1) Profile Picture
2) Username
3) Name
4) Tweet content
4) Likes
'''

def generate_pfp():
    pfp = duck.get_duck()
    return pfp

def generate_content_riddle():
    return riddle.get_url()

def generate_content_uselessfacts():
    return uselessfacts.get_fact()

def generate_content():
    # num = random.randint(0,1)
    # content = None
    # if (num == 0):
    #     content = generate_content_riddle()
    # else:
    #     content = generate_content_uselessfacts()
    # return content
    return generate_content_uselessfacts()

def generate_tweet(username, name):
    db.tweet_table_init()
    db.create_tweet(generate_pfp(), username, name, generate_content(), random.randint(1,100000))

def return_tweets():
    return db.return_tweets()





    




