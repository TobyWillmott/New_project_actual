import requests
import json

def main():
    url = "https://fantasy.premierleague.com/api/fixtures/"
    response = requests.get(url)
    data = response.text
    parse_json = json.loads(data)
    print(parse_json)

main()