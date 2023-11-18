import tkinter as tk


class Registration(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(background="#E5E5E5")

        self.title_label = tk.Label(self,
                                    text="Welcome to football survivor",
                                    bg="#e7e6ed", fg="black",
                                    width=0,
                                    font=("Arial", 25))

        self.controller = parent
        self.label_first_name = tk.Label(self, text="First Name:", bg="#E5E5E5", fg="black")

        self.label_second_name = tk.Label(self, text="Second Name:", bg="#E5E5E5", fg="black")

        # label
        self.label_username = tk.Label(self, text="Username:", bg="#E5E5E5", fg="black")

        self.label_password = tk.Label(self, text='Password: ', bg="#E5E5E5", fg="black")

        self.first_name_var = tk.StringVar()
        self.first_name_entry = tk.Entry(self, textvariable=self.first_name_var, width=30, font=('Arial', 20), bg="white")

        self.second_name_var = tk.StringVar()
        self.second_name_entry = tk.Entry(self, textvariable=self.second_name_var, width=30, font=('Arial', 20), bg="white")

        # username entry
        self.username_var = tk.StringVar()
        self.username_entry = tk.Entry(self, textvariable=self.username_var, width=30, font=('Arial', 20), bg="white")

        # password entry
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(self, textvariable=self.password_var, width=30, font=('Arial', 20), bg="white")

        # save button
        self.save_button = tk.Button(self, text='Save', command=self.save_button_clicked)

        # message
        self.message_label = tk.Label(self, text='', foreground='red', bg="red")

        self.back_button = tk.Button(self, text="Back", command=self.back_clicked)

        # set the controller

        self.place_widgets()

    def place_widgets(self):
        self.label_first_name.place(x=200, y=50)
        self.label_second_name.place(x=200, y=130)
        self.first_name_entry.place(x=200, y=80)
        self.second_name_entry.place(x=200, y=160)
        self.label_username.place(x=200, y=210)
        self.label_password.place(x=200, y=290)
        self.username_entry.place(x=200, y=240)
        self.password_entry.place(x=200, y=320)
        self.title_label.place(x=200, y=0)
        self.save_button.place(x=200, y=380)
        self.message_label.place(x=200, y=350)
        self.back_button.place(x=0, y=0)

    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        try:
            if self.controller:
                clicked = self.controller.add_user(self.first_name_var.get(), self.second_name_var.get(),
                                                   self.username_var.get(), self.password_var.get())
                # self.show_success(clicked)
                self.show_home_page()
        except ValueError as error:
            self.show_error(error)

    def show_home_page(self):
        self.user_list = self.controller.get_username_details(self.username_var.get())
        id = self.user_list[0]
        self.controller.show_home_page(id)

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.username_entry['foreground'] = 'red'
        self.password_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.username_entry['foreground'] = 'black'
        self.username_var.set('')
        self.password_var.set('')
        self.first_name_var.set('')
        self.second_name_var.set('')

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''

    def revert_colours(self):
        self.password_entry["foreground"] = "black"
        self.username_entry["foreground"] = "black"

    def back_clicked(self):
        self.controller.show_frame("sign_in_frame")
