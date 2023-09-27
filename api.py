import requests
import json


# https://fantasy.premierleague.com/api/fixtures/?event=1
# https://fantasy.premierleague.com/api/fixtures/?event={event_id}
# https://fantasy.premierleague.com/api/fixtures/

def match_info(game_week_id):
    url = f"https://fantasy.premierleague.com/api/fixtures/?event={game_week_id}"
    response = requests.get(url)
    data = response.text
    parse_json = json.loads(data)
    lis_game_week = []
    lis = []
    for active_case in parse_json:
        lis = [active_case['team_h'], active_case['team_h_difficulty'], active_case['team_a'], active_case['team_a_difficulty']]
        lis_game_week.append(lis)
    return lis_game_week

def check_lives(starting_gameweek, user_id, league_id):
    param = {'team_a' : 1}
    url = "https://fantasy.premierleague.com/api/fixtures/"
    response = requests.get(url)
    data = response.json()
    print(data)


check_lives(1)
