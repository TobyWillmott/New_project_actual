import tkinter as tk

class Registration(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        self.controller = parent
        self.label_first_name = tk.Label(self, text="First Name:")
        self.label_first_name.grid(row=1, column=0)

        self.label_second_name = tk.Label(self, text="Second Name:")
        self.label_second_name.grid(row=2, column=0)
        # label
        self.label_username = tk.Label(self, text="Username:")
        self.label_username.grid(row=3, column=0)

        self.label_password = tk.Label(self, text='Password: ')
        self.label_password.grid(row=4, column=0)

        self.first_name_var = tk.StringVar()
        self.first_name_entry = tk.Entry(self, textvariable=self.first_name_var, width=30)
        self.first_name_entry.grid(row=1, column=1)

        self.second_name_var = tk.StringVar()
        self.second_name_entry = tk.Entry(self, textvariable=self.second_name_var, width=30)
        self.second_name_entry.grid(row=2, column=1)

        # username entry
        self.username_var = tk.StringVar()
        self.username_entry = tk.Entry(self, textvariable=self.username_var, width=30)
        self.username_entry.grid(row=3, column=1, sticky=tk.NSEW)

        # password entry
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(self, textvariable=self.password_var, width=30)
        self.password_entry.grid(row=4, column=1, sticky=tk.NSEW)

        # save button
        self.save_button = tk.Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=4, column=3, padx=10)

        # message
        self.message_label = tk.Label(self, text='', foreground='red')
        self.message_label.grid(row=3, column=1, sticky=tk.W)

        self.back_button = tk.Button(self, text="Back", command=self.back_clicked)
        self.back_button.grid(row=0, column=0)
        # set the controller



    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        try:
            if self.controller:
                clicked = self.controller.add_user(self.first_name_var.get(), self.second_name_var.get(),
                                               self.username_var.get(), self.password_var.get())
                #self.show_success(clicked)
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
        self.controller.show_frame("welcome_frame")


