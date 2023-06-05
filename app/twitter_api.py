import tweepy

#read all of the API information into their respective variables

#init api_key
api_file = open("keys/twitter/api_key.txt", "r")
api_key = api_file.read()
api_file.close()

#init api_key_secret
api_secret_file = open("keys/twitter/api_key_secret.txt","r")
api_key_secret = api_secret_file.read()
api_secret_file.close()

#init access_token
access_file = open("keys/twitter/access_token.txt","r")
access_token = access_file.read()
access_file.close()

#init access_token_secret
access_secret_file = open("keys/twitter/access_token_secret.txt","r")
access_token_secret = access_secret_file.read()
access_secret_file.close()

#init bearer_token
bearer_file = open("keys/twitter/bearer_token.txt","r")
bearer_token = bearer_file.read()
bearer_file.close()

def printKeys():
    print("api key: " + api_key)
    print("api_key_secret: " + api_key_secret)
    print("access_token: " + access_token)
    print("access_token_secret: " + access_token_secret)
    print("bearer_token: " + bearer_token)

printKeys()
