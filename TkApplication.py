from sqlalchemy import create_engine
from models import Base

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



if __name__ == "__main__":
    # engine = create_engine("sqlite:///fantasy_football.db", echo=True)
    # Base.metadata.create_all(engine)
    
    # app = TkApplication()
    # app.mainloop()
    from api import main
    main()


