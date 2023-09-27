from registration_GUI import Registration
from welcome_GUI import WelcomeScreen
from sign_in_GUI import SignIn
from create_league_GUI import CreateLeague
import tkinter as tk
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import User, League, UserLeague, Gameweek, Selection, Team
from home_screen_GUI import HomeScreen
from select_teams_GUI import SelectTeams
import requests
import json
from view_league_GUI import ViewLeague
from game_objects import Game


class TkApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.game = Game()

        title_string = "Fantasy football"
        self.title(title_string)
        self.resizable(False, False)

        self.engine = create_engine("sqlite:///fantasy_football.db", echo=True)
        title_label = tk.Label(self,
                               text=title_string,
                               bg="#e7e6ed", fg="black",
                               width=60,
                               font=("Arial", 25))
        title_label.pack(side=tk.TOP)

        self.frames = {
            "welcome_frame": WelcomeScreen(self),
            "sign_in_frame": SignIn(self),
            "register_frame": Registration(self)
        }

        self.show_frame("sign_in_frame")

    def show_frame(self, current_frame: str):
        widgets = self.winfo_children()
        for w in widgets:
            if w.winfo_class() == "Frame":
                w.pack_forget()

        frame_to_show = self.frames[current_frame]
        frame_to_show.pack(expand=True, fill=tk.BOTH)

    def show_home_page(self, user_id):
        widgets = self.winfo_children()
        for w in widgets:
            if w.winfo_class() == "Frame":
                w.pack_forget()

        frame_to_show = HomeScreen(self, user_id)
        frame_to_show.pack(expand=True, fill=tk.BOTH)

    def show_create_league_page(self, user_id):
        widgets = self.winfo_children()
        for w in widgets:
            if w.winfo_class() == "Frame":
                w.pack_forget()

        frame_to_show = CreateLeague(self, user_id)
        frame_to_show.pack(expand=True, fill=tk.BOTH)

    def show_league_selection_page(self, user_id, league_id, gameweek_id):
        widgets = self.winfo_children()
        for w in widgets:
            if w.winfo_class() == "Frame":
                w.pack_forget()

        frame_to_show = SelectTeams(self, user_id, league_id, gameweek_id)
        frame_to_show.pack(expand=True, fill=tk.BOTH)

    def show_view_league_page(self, user_id, league_id):
        widgets = self.winfo_children()
        for w in widgets:
            if w.winfo_class() == "Frame":
                w.pack_forget()

        frame_to_show = ViewLeague(self, user_id, league_id)
        frame_to_show.pack(expand=True, fill=tk.BOTH)

    def add_user(self, first_name_, last_name_, username_, password_):
        self.game.add_user(first_name_, last_name_, username_, password_)

    def get_username_details(self, username_entry):
        self.game.get_username_details(username_entry)

    def get_gameweek_timings(self):
        self.game.get_gameweek_timings()

    def get_gameweek_id(self):
        self.game.get_gameweek_id()

    def add_selection_list(self, user_selections):
        with Session(self.engine) as sess:
            sess.add_all(user_selections)
            sess.commit()

    def add_selection(self, gameweek_id_, user_id_, team_id_, league_id_):
        with Session(self.engine) as sess:
            user_selection = Selection(gameweek_id=gameweek_id_, outcome=None, user_id=user_id_, team_id=team_id_,
                                       league_id=league_id_)
            sess.add(user_selection)
            sess.commit()

    def get_teams(self):
        with Session(self.engine) as sess:
            teams = sess.query(Team.team_id, Team.team_name).all()
        lis = []
        for i in teams:
            lis.append(i)
        return lis

    def get_league_starting_gameweek(self, league_id_):
        with Session(self.engine) as sess:
            gameweek = sess.query(League.gameweek_id).filter_by(league_id=league_id_).first()
        return gameweek[0]

    def get_final_league_gameweek(self):
        with Session(self.engine) as sess:
            gameweek_id = sess.query(League.league_id, League.gameweek_id).order_by(League.league_id.desc()).first()
        return gameweek_id

    def get_user_league_info(self, user_id_):
        with Session(self.engine) as sess:
            league_ids = sess.query(UserLeague.league_id).filter_by(user_id=user_id_).all()
        lis = []
        for i in league_ids:
            lis.append(i[0])
        with Session(self.engine) as sess:
            output_lis = []
            for j in lis:
                league_info = sess.query(League.league_id, League.league_name, League.gameweek_id).filter_by(
                    league_id=j).first()
                output_lis.append(league_info)
        return output_lis

    def match_info(self, game_week_id):
        url = f"https://fantasy.premierleague.com/api/fixtures/?event={game_week_id}"
        response = requests.get(url)
        data = response.text
        parse_json = json.loads(data)
        lis_game_week = []
        for active_case in parse_json:
            lis = [active_case['team_h'], active_case['team_h_difficulty'], active_case['team_a'],
                   active_case['team_a_difficulty']]
            lis_game_week.append(lis)
        return lis_game_week

    def id_to_team(self, team_id_):
        with Session(self.engine) as sess:
            team_name = sess.query(Team.team_name).filter_by(team_id=team_id_).first()
        return team_name[0]

    def get_user_name(self, user_ids):
        with Session(self.engine) as sess:
            user_names = []
            for user_id in user_ids:
                user_name = sess.query(User.first_name, User.last_name).filter_by(user_id=user_id[0]).first()
                user_names.append(user_name)
        return user_names

    def get_user_ids(self, league_id_):
        with Session(self.engine) as sess:
            user_ids = sess.query(UserLeague.user_id).filter_by(league_id=league_id_).all()
        return user_ids

    def get_selection(self, user_id_, league_id_):
        with Session(self.engine) as sess:
            selections = sess.query(Selection.team_id, Selection.gameweek_id).filter_by(user_id=user_id_,
                                                                                        league_id=league_id_).all()
        return selections

    def check_lives(self, user_ids, league_id):
        url = "https://fantasy.premierleague.com/api/fixtures/"
        lives = []
        response = requests.get(url)
        data = response.json()
        for user in range(len(user_ids)):
            num_lives = 10
            user_selections = self.get_selection(user_ids[user][0], league_id)
            print(user_selections)
            for team_id, gameweek_id in user_selections:
                for match in data:
                    if match["event"] == gameweek_id and (match["team_a"] == team_id or match["team_h"] == team_id):
                        if match["team_a"] == team_id:
                            if match["team_a_score"] is None or match["team_h_score"] is None:
                                break
                            elif match["team_a_score"] == match["team_h_score"]:
                                num_lives -= 1
                            elif match["team_a_score"] < match["team_h_score"]:
                                num_lives -= 2
                        elif match["team_h"] == team_id:
                            if match["team_a_score"] is None or match["team_h_score"] is None:
                                break
                            elif match["team_a_score"] == match["team_h_score"]:
                                num_lives -= 1
                            elif match["team_a_score"] > match["team_h_score"]:
                                num_lives -= 2
            lives.append(num_lives)
        return lives


if __name__ == "__main__":
    app = TkApplication()
    app.mainloop()
