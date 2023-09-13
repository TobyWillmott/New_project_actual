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
    for active_case in parse_json:
        lis = [f"event {active_case['event']}", f"kickoff_time {active_case['kickoff_time']}",
               f"team_h {active_case['team_h']}", f"team_h_score {active_case['team_h_score']}", f"team_h_difficulty {active_case['team_h_difficulty']}",
               f"team_a {active_case['team_a']}", f"team_a_score {active_case['team_a_score']}", f"team_a_difficulty {active_case['team_a_difficulty']}"]
        lis_game_week.append(lis)
    return lis_game_week


print(match_info(1))
