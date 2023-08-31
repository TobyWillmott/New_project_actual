import tkinter as tk

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
        self.place_widgets()

    def place_widgets(self):
        self.create_league_button.grid(row=1, column=0)

        self.join_league_entry.grid(row=2, column=1)
        self.join_league_button.grid(row=2, column=2)
        self.join_league_text.grid(row=2, column=0)
        self.id_label.grid(row=4, column=0)

    def join_league_clicked(self):
        self.controller.add_user_league(self.user_id, self.join_league_var.get())

    def create_league_clicked(self):
        self.controller.show_frame("create_league_frame")