import tkinter as tk


class SignIn(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = parent
        self.configure(background="#E5E5E5")
        self.title_label = tk.Label(self,
                                    text="Welcome to football survivor",
                                    bg="#e7e6ed", fg="black",
                                    width=0,
                                    font=("Arial", 25))
        self.view_password_logo = {"view": tk.PhotoImage(file=r"images/view.png").subsample(19,19),
                                   "hide": tk.PhotoImage(file=r"images/hide.png").subsample(19,19)}
        self.view_button = tk.Button(self, image=self.view_password_logo["view"], command=self.view_clicked)
        self.label_username = tk.Label(self, text="Username:", bg="#E5E5E5", fg="black")
        self.label_password = tk.Label(self, text='Password: ', bg="#E5E5E5", fg="black")
        self.username_var = tk.StringVar()
        self.username_entry = tk.Entry(self, textvariable=self.username_var, width=32, bg="white", font=('Arial', 20),
                                       fg="black")
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(self, textvariable=self.password_var, width=32, bg="white", font=('Arial', 20),
                                       fg="black", show="*")
        self.enter_button = tk.Button(self, text='Login', command=self.enter_button_clicked, padx=166, pady=12, highlightbackground="#E5E5E5")
        self.register_label = tk.Label(self, text="No account?", bg="#E5E5E5", fg="black" )
        self.register_button = tk.Button(self, text="Create one", command=self.register_clicked,
                                         bg="#E5E5E5", fg="blue", font=('Arial', 12, 'underline'), highlightbackground="#E5E5E5")
        self.error_message = tk.Label(self, text="", fg="red", bg="#E5E5E5", font=('Arial', 17))
        self.place_widgets()

    def place_widgets(self):
        self.label_username.place(x=200, y=85)
        self.label_password.place(x=200, y=170)
        self.username_entry.place(x=200, y=115)
        self.password_entry.place(x=200, y=200)
        self.enter_button.place(x=200, y=295)
        self.register_label.place(x=319, y=350)
        self.register_button.place(x=400, y=350)
        self.title_label.place(x=200, y=20)
        self.error_message.place(x=330, y=260)
        self.view_button.place(x=560, y=200)
        self.view_button.lift()

    def enter_button_clicked(self):
        self.user_list = self.controller.get_username_details(self.username_var.get())
        if self.user_list is None:
            self.error_message.configure(text="Incorrect Username")
        else:
            password = self.controller.hash_password(self.password_var.get())
            if password == self.user_list[2]:
                self.show_home_page(self.user_list[0])
            else:
                self.error_message.configure(text="Incorrect Password")

    def show_home_page(self, id):
        self.controller.show_home_page(id)
    def view_clicked(self):
        if self.view_button.cget('image')==str(self.view_password_logo["view"]):
            self.view_button.configure(image=self.view_password_logo["hide"])
            self.password_entry.configure(show="")

        elif self.view_button.cget('image') == str(self.view_password_logo["hide"]):
            self.view_button.configure(image=self.view_password_logo["view"])
            self.password_entry.configure(show="*")
    def show_error(self):
        print("not a Valid_username")

    def register_clicked(self):
        self.controller.show_frame("register_frame")
