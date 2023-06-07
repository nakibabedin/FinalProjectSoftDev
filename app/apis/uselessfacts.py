import requests

def get_fact():
    link = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
    return requests.get(link).json()

print(get_fact())