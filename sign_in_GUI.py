import tkinter as tk


class SignIn(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = parent
        self.label_username = tk.Label(self, text="Username:")
        self.label_username.grid(row=3, column=0)

        self.label_password = tk.Label(self, text='Password: ')
        self.label_password.grid(row=4, column=0)

        self.username_var = tk.StringVar()
        self.username_entry = tk.Entry(self, textvariable=self.username_var, width=30)
        self.username_entry.grid(row=3, column=1, sticky=tk.NSEW)

        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(self, textvariable=self.password_var, width=30)
        self.password_entry.grid(row=4, column=1, sticky=tk.NSEW)

        self.enter_button = tk.Button(self, text='Enter', command=self.enter_button_clicked)
        self.enter_button.grid(row=4, column=3, padx=10)

        self.back_button = tk.Button(self, text="Back", command=self.back_clicked)
        self.back_button.grid(row=0, column=0)

    def back_clicked(self):
        self.controller.show_frame("welcome_frame")

    def enter_button_clicked(self):
        self.user_list = self.controller.get_username_details(self.username_var.get())
        print(self.user_list)
        if self.user_list is None:
            print("username not right")
        else:
            if self.user_list[2] == self.password_var.get():
                self.show_home_page(self.user_list[0])
            else:
                print("password incorrect")

    def show_home_page(self, id):
        self.controller.show_home_page(id)

    def show_error(self):
        print("not a Valid_username")
