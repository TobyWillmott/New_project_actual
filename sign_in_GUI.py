import tkinter as tk
from controller import Controller
import tkinter.ttk as ttk


class SignIn(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

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

        self.enter_button = tk.Button(self, text='Save', command=self.enter_button_clicked)
        self.enter_button.grid(row=4, column=3, padx=10)

        self.controller = None

    def enter_button_clicked(self):
        pass

    def set_controller(self, controller):
        self.controller = controller

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Registration Screen')

        # create a view and place it on the root window
        view = SignIn(self)
        view.grid(row=0, column=0, padx=50, pady=50)

        # create a controller
        controller = Controller()

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
