import tweepy

#read all of the API information into their respective variables

#init api_key
api_file = open("../keys/twitter/api_key.txt", "r")
api_key = api_file.read()
api_file.close()

#init api_key_secret
api_secret_file = open("../keys/twitter/api_key_secret.txt","r")
api_key_secret = api_secret_file.read()
api_secret_file.close()

#init access_token
access_file = open("../keys/twitter/access_token.txt","r")
access_token = access_file.read()
access_file.close()

#init access_token_secret
access_secret_file = open("../keys/twitter/access_token_secret.txt","r")
access_token_secret = access_secret_file.read()
access_secret_file.close()

#init bearer_token
bearer_file = open("../keys/twitter/bearer_token.txt","r")
bearer_token = bearer_file.read()
bearer_file.close()

def printKeys():
    print("api key: " + api_key)
    print("api_key_secret: " + api_key_secret)
    print("access_token: " + access_token)
    print("access_token_secret: " + access_token_secret)
    print("bearer_token: " + bearer_token)

## Test if keys are assigned the desired value
#printKeys()

# set up OAuth
auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Testing how to get tweet timeline
# public_tweets = api.home_timeline()
# print(public_tweets)
# curl "https://api.twitter.com/2/users/by/username/$FortniteSoftDev" -H "Authorization: Bearer $"









