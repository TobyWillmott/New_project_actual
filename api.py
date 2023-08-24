import requests

def main():
    url = "https://fantasy.premierleague.com/api/fixtures/"
    response = requests.get(url)
    json = response.json()