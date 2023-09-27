import tkinter as tk
from functools import partial


class HomeScreen(tk.Frame):
    def __init__(self, parent, user_id):
        super().__init__(parent)

        self.user_id = user_id
        self.controller = parent
        self.create_league_button = tk.Button(self, text="Create League", command=self.create_league_clicked)
        self.join_league_var = tk.StringVar()
        self.join_league_entry = tk.Entry(self, textvariable=self.join_league_var, width=30)
        self.join_league_button = tk.Button(self, text="Join", command=self.join_league_clicked)
        self.join_league_text = tk.Label(self, text="To join league enter unique id")
        self.id_label = tk.Label(self, text=self.user_id)
        self.user_leagues = self.controller.get_user_league_info(self.user_id)

        self.league_id_label = tk.Label(self, text="League ID")
        self.league_name_label = tk.Label(self, text="League Name")
        self.start_gameweek_label = tk.Label(self, text="Start Gameweek")
        self.league_id = [tk.Button(self, text=name[0], command=partial(self.view_league_clicked, name[0])) for name in
                          self.user_leagues]
        self.league_name = [tk.Label(self, text=name[1]) for name in self.user_leagues]
        self.start_gameweek = [tk.Label(self, text=name[2]) for name in self.user_leagues]

        self.place_widgets()

    def place_widgets(self):
        self.create_league_button.grid(row=1, column=0)
        self.join_league_entry.grid(row=2, column=1)
        self.join_league_button.grid(row=2, column=2)
        self.join_league_text.grid(row=2, column=0)
        self.id_label.grid(row=4, column=0)
        self.league_id_label.grid(row=5, column=0)
        self.league_name_label.grid(row=5, column=1)
        self.start_gameweek_label.grid(row=5, column=2)
        for i in range(len(self.league_id)):
            self.league_id[i].grid(row=6 + i, column=0)
            self.league_name[i].grid(row=6 + i, column=1)
            self.start_gameweek[i].grid(row=6 + i, column=2)

    def join_league_clicked(self):
        self.controller.add_user_league(self.user_id, self.join_league_var.get())
        current_gameweek = self.controller.get_league_starting_gameweek(self.join_league_var.get())
        self.controller.show_league_selection_page(self.user_id, self.join_league_var.get(), current_gameweek)

    def create_league_clicked(self):
        self.controller.show_create_league_page(self.user_id)

    def view_league_clicked(self, league_id):
        self.controller.show_view_league_page(self.user_id, league_id)
