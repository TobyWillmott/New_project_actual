import tkinter as tk

class ViewLeague(tk.Frame):
    def __init__(self, parent, user_id, league_id):
        super().__init__(parent)

        self.user_id = user_id
        self.league_id = league_id
        self.controller = parent

        self.user_ids = self.controller.get_user_ids(self.league_id)
        self.user_names = self.controller.get_user_name(self.user_ids)
        self.lives = self.controller.check_lives(self.user_ids, self.league_id)
        print("lives", self.lives)
        self.total_list = []
        for i in range(len(self.user_ids)):
            lis=[]
            lis.append(self.user_ids[i][0])
            lis.append(self.user_names[i])
            lis.append(self.lives[i])
            self.total_list.append(lis)
        self.total_list.sort(reverse=True, key=lambda x:x[2])
        self.position_label = tk.Label(self, text="Positon")
        self.user_label = tk.Label(self, text="Name")
        self.lives_label = tk.Label(self, text="Number of lives")

        self.positions = [tk.Label(self, text=f"{position+1}") for position in range(len(self.user_ids))]
        self.user_names = [tk.Label(self, text=f"{name[1][0]} {name[1][1]}") for name in self.total_list]
        self.back_button = tk.Button(self, text="Back", command=self.back_clicked)
        self.user_lives = [tk.Label(self, text=f"{lives[2]}") for lives in self.total_list]

        self.place_widgets()

    def place_widgets(self):
        self.position_label.grid(row=1, column=0)
        self.user_label.grid(row=1, column=1)
        self.lives_label.grid(row=1, column=2)
        self.back_button.grid(row=0, column=0)

        for i in range(len(self.user_ids)):
            self.positions[i].grid(row=2+i, column=0)
            self.user_names[i].grid(row=2+i, column=1)
            self.user_lives[i].grid(row=2+i, column=3)


    def back_clicked(self):
        self.controller.show_home_page(self.user_id)