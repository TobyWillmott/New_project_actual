import queries as qry
import api as api




class Game():

    def __init__(self):
        self.user = None
    def add_user(self, first_name_, last_name_, username_, password_):
        qry.qry_add_user(first_name_, last_name_, username_, password_)
    def get_gameweek_timings(self):
        return qry.qry_get_gameweek_timings()
    def add_league(self, gameweek_id_, league_name_):
        qry.qry_add_league(gameweek_id_, league_name_)
    def add_user_league(self, user_id_, league_id_):
        qry.qry_add_user_league(user_id_, league_id_)
    def add_selection_list(self, user_selections):
        qry.qry_add_selection_list(user_selections)
    def get_gameweek_id(self):
        return qry.qry_get_gameweek_id()
    def get_username_details(self, username_entry):
        return qry.qry_get_username_details(username_entry)
    def add_selection(self, gameweek_id_, user_id_, team_id_, league_id_):
        qry.qry_add_selection(gameweek_id_, user_id_, team_id_, league_id_)
    def get_teams(self):
        return qry.qry_get_teams()
    def get_league_starting_gameweek(self, league_id_):
        return qry.qry_get_league_starting_gameweek(league_id_)
    def get_final_league_gameweek(self):
        return qry.qry_get_final_league_gameweek()
    def get_user_league_info(self, user_id_):
        return qry.qry_get_user_league_info(user_id_)
    def id_to_team(self, team_id_):
        return qry.qry_id_to_team(team_id_)
    def get_user_name(self, user_ids):
        return qry.qry_get_user_name(user_ids)
    def get_user_ids(self, league_id_):
        return qry.qry_get_user_ids(league_id_)
    def get_selection(self, user_id_, league_id_):
        return qry.qry_get_selection(user_id_, league_id_)
    def match_info(self, game_week_id):
        return api.api_match_info(game_week_id)
    def check_lives(self, user_ids, league_id):
        return api.api_check_lives(user_ids, league_id)
