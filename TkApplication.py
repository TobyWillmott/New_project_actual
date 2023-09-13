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


class TkApplication(tk.Tk):
    def __init__(self):
        super().__init__()

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

    def add_user(self, first_name_, last_name_, username_, password_):
        try:

            with Session(self.engine) as sess:
                user = User(first_name=first_name_, last_name=last_name_, username=username_, password=password_)
                sess.add(user)
                sess.commit()

                return f"It worked"

        except ValueError as error:
            # show an error message
            raise ValueError(error)

    def add_league(self, gameweek_id_, league_name_):
        with Session(self.engine) as sess:
            league = League(gameweek_id=gameweek_id_, league_name=league_name_)
            sess.add(league)
            sess.commit()

    def add_user_league(self, user_id_, league_id_):
        with Session(self.engine) as sess:
            user_league_value = UserLeague(user_id=user_id_, league_id=league_id_)
            sess.add(user_league_value)
            sess.commit()

    def get_username_details(self, username_entry):
        with Session(self.engine) as sess:
            output_lis = sess.query(User.user_id, User.username, User.password).filter_by(
                username=username_entry).first()
        return output_lis

    def get_gameweek_timings(self):
        with Session(self.engine) as sess:
            output_lis = sess.query(Gameweek.start_date).all()
        return output_lis

    def get_gameweek_id(self):
        with Session(self.engine) as sess:
            output_id = sess.query(Gameweek.gameweek_id, Gameweek.start_date).all()
        return output_id

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
        print(gameweek_id)
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


if __name__ == "__main__":
    app = TkApplication()
    app.mainloop()
    from api import main

    main()
