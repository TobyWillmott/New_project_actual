import tkinter as tk
from functools import partial
from models import Selection


class SelectTeams(tk.Frame):
    def __init__(self, parent, user_id, league_id, gameweek_id):
        super().__init__(parent)

        self.config(background="#E5E5E5")
        self.controller = parent
        self.user_id = user_id
        self.league_id = league_id
        self.teams_id = self.controller.get_teams()
        self.teams = self.get_teams()
        self.current_gameweek_id = tk.IntVar()
        self.current_gameweek_id.set(gameweek_id)
        self.start_gameweek = gameweek_id
        self.teams_buttons = [
            tk.Button(self, bg="white", text=f"{name}\n", font=('Arial', 10), fg="black",
                      command=partial(self.choose_team, name), highlightbackground="#E5E5E5", width=13) for name in
            self.teams]
        self.gameweek_label = tk.Label(self,
                                       text=f"The gameweek to choose a team for is {self.current_gameweek_id.get()}")
        self.select_button = tk.Button(self, text="Confirm", command=self.select_picked)
        self.user_selection = []
        self.place_widgets()

    def place_widgets(self):
        self.gameweek_label.place(x=10, y=10)
        index = 0
        row_index = 0
        column_index = 0
        for i in self.teams_buttons:
            if index % 5 == 0:
                row_index += 1
            i.place(x=(column_index % 5) * 125, y=20 + row_index * 40)
            column_index += 1
            index += 1
        self.select_button.grid(row=8, column=0)
        self.display_matches()

    def display_matches(self):
        matches = self.controller.match_info(self.current_gameweek_id.get())
        matches_teams = []
        for match in matches:
            home_difficulty= self.calculate_colour(match[1])
            away_difficulty = self.calculate_colour(match[3])
            lis = [self.controller.id_to_team(match[0]), self.controller.id_to_team(match[2]), home_difficulty, away_difficulty]
            matches_teams.append(lis)
        index = 0
        self.home_teams = [tk.Label(self, text=match[0], fg="black", bg=match[2], width=3) for match in matches_teams]
        self.away_teams = [tk.Label(self, text=match[1], fg="black", bg=match[3], width=3) for match in matches_teams]
        self.versus_label = [tk.Label(self, text="vs", fg="black", bg="#E5E5E5") for j in range(len(matches))]
        for i in range(len(matches)):
            self.home_teams[i].place(x=650, y=50+index*30)
            self.away_teams[i].place(x=750, y=50+index*30)
            self.versus_label[i].place(x=708, y=50+index*30)
            index += 1
    def calculate_colour(self, difficulty):
        if difficulty==1:
            colour="#2cba00"
        elif difficulty==2:
            colour="#a3ff00"
        elif difficulty==3:
            colour="#fff400"
        elif difficulty==4:
            colour="#ffa700"
        elif difficulty==5:
            colour="#ff0000"
        return colour


    def display_matches_second(self):
        matches = self.controller.match_info(self.current_gameweek_id.get())
        matches_teams = []
        for match in matches:
            lis = [self.controller.id_to_team(match[0]), self.controller.id_to_team(match[2])]
            matches_teams.append(lis)
        index = 0
        matches = self.controller.match_info(self.current_gameweek_id.get())
        matches_teams = []
        for match in matches:
            lis = [self.controller.id_to_team(match[0]), self.controller.id_to_team(match[2])]
            matches_teams.append(lis)
        index = 0
        for i in range(len(matches)):
            self.home_teams[i].configure(text=matches_teams[i][0])
            self.away_teams[i].configure(text=matches_teams[i][1])
            self.home_teams[i].place(x=650, y=50+index*30)
            self.away_teams[i].place(x=750, y=50+index*30)
            index += 1

    def get_teams(self):
        teams_lis = []
        for i in self.teams_id:
            teams_lis.append(i[1])
        return teams_lis

    def choose_team(self, name):
        team_id = None
        for i in self.teams_id:
            if i[1] == name:
                team_id = i[0]
        self.team_id = team_id

    def select_picked(self):
        self.user_selection.append(
            Selection(gameweek_id=self.current_gameweek_id.get(), outcome=None, user_id=self.user_id,
                      team_id=self.team_id,
                      league_id=self.league_id))
        self.teams_buttons[self.team_id - 1].configure(bg="grey",
                                                       text=f"{self.teams_id[self.team_id - 1][1]}\n{self.current_gameweek_id.get()}")
        current_num = self.current_gameweek_id.get()
        current_num += 1
        self.current_gameweek_id.set(current_num)
        self.gameweek_label.configure(text=f"The gameweek to choose a team for is {self.current_gameweek_id.get()}")
        self.display_matches_second()
        if self.check_gameweek():
            self.finished_selection()

    def check_gameweek(self):
        if self.current_gameweek_id.get() == self.start_gameweek + 20:
            print("found")
            return True
        else:
            return False

    def finished_selection(self):
        self.controller.add_selection_list(self.user_selection)
        self.return_home = tk.Button(self, text="Return to homepage", command=self.return_home_page)
        self.return_home.grid(row=20, column=2)

    def return_home_page(self):
        self.controller.show_home_page(self.user_id)
