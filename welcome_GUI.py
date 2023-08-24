import tkinter as tk
from controller import Controller
from TkApplication import TkApplication
class WelcomeScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.welcome_label = tk.Label(self, text="Username:")
        self.sign_in_button = tk.Button(self, text="Sign in", command=self.sign_in_clicked)
        self.register_button = tk.Button(self, text="Register", command=self.register_clicked)

        self.place_widgets()

    def place_widgets(self):
        self.welcome_label.grid(row=1, column=0)
        self.sign_in_button.grid(row=2, column=0)
        self.register_button.grid(row=2, column=1)

    def sign_in_clicked(self):
        from TkApplication import TkApplication
        self.TkApplication.show_frame(sign_in_frame)

    def register_clicked(self):
        pass

    def set_controller(self, controller):
        self.controller = controller

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Registration Screen')

        # create a view and place it on the root window
        view = WelcomeScreen(self)
        view.grid(row=0, column=0, padx=50, pady=50)

        # create a controller
        controller = Controller()

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()