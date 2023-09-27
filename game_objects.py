import queries as qry

class Game():

    def __init__(self):
        self.user = None

    def add_user(self, first_name_, last_name_, username_, password_):
        qry.qry_add_user(first_name_, last_name_, username_, password_)

    def get_username_details(self, username_entry):
        qry.qry_get_username_details(username_entry)

    def get_gameweek_timings(self):
        qry.qry_get_gameweek_timings()

    def get_gameweek_id(self):
        qry.qry_get_gamewek_id()


