from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import User


class Controller:
    def __init__(self):
        self.engine = create_engine("sqlite:///fantasy_football.db", echo=True)

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
