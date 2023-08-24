from registration_GUI import Registration
from welcome_GUI import WelcomeScreen
from sign_in_GUI import SignIn
import tkinter as tk

class TkApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        title_string = "Fantasy football"
        self.title(title_string)
        self.resizable(False, False)

        title_label = tk.Label(self,
                               text=title_string,
                               bg="#e7e6ed", fg="black",
                               width=60,
                               font=("Arial", 25))
        title_label.pack(side=tk.TOP)

        self.frames = {
            "welcome_frame": WelcomeScreen(self),
            "sign_in_frame": SignIn(self),
            "register_frame": Registration(self),
        }

        self.show_frame("welcome_frame")

    def show_frame(self, current_frame: str):
        widgets = self.winfo_children()
        for w in widgets:
            if w.winfo_class() == "Frame":
                w.pack_forget()

        frame_to_show = self.frames[current_frame]
        frame_to_show.pack(expand=True, fill=tk.BOTH)

    def save(self, first_name_, last_name_, username_, password_):
        """
        Save the email
        :param password_:
        :param first_name_:
        :param username_:
        :param last_name_:
        :return:
        """
        try:

            with Session(self.engine) as sess:
                user = User(first_name=first_name_, last_name=last_name_, username=username_, password=password_)
                sess.add(user)
                sess.commit()

                return f"It worked"

        except ValueError as error:
            # show an error message
            raise ValueError(error)

if __name__ == "__main__":
    app = TkApplication()
    app.mainloop()


