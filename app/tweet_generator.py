from apis import duck, riddle, uselessfacts, twitter_api
import random
'''
Tweet Components:
1) Profile Picture
2) Username
3) Name
4) Tweet content
4) Likes
5) Comments
'''

def generate_pfp():
    pfp = duck.get_duck()
    return pfp

def generate_content_riddle():
    return riddle.get_url()

def generate_content_uselessfacts():
    return uselessfacts.get_fact()

def generate_content():
    num = random.randint(0,1)
    content = None
    if (num == 0):
        content = generate_content_riddle()
    else:
        content = generate_content_uselessfacts()




