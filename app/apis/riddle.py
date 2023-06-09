import requests

api_file = open("../keys/riddles.txt")
api_key = api_file.read()
api_file.close()

def get_url():
    api_url = 'https://api.api-ninjas.com/v1/riddles'
    return requests.get(api_url, headers={'X-Api-Key': api_key}).json()

print(get_url())