from sqlalchemy import create_engine
from models import Base, User, Gameweek
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///fantasy_football.db", echo=True)
Base.metadata.create_all(engine)


def qry_add_user(first_name_, last_name_, username_, password_):
    try:

        with Session(engine) as sess:
            user = User(first_name=first_name_, last_name=last_name_, username=username_, password=password_)
            sess.add(user)
            sess.commit()

            return f"It worked"

    except ValueError as error:
        # show an error message
        raise ValueError(error)


def qry_get_username_details(username_entry):
    with Session(self.engine) as sess:
        output_lis = sess.query(User.user_id, User.username, User.password).filter_by(
            username=username_entry).first()
    return output_lis


def qry_get_gameweek_timings():
    with Session(self.engine) as sess:
        output_lis = sess.query(Gameweek.start_date).all()
    return output_lis


def qry_get_gameweek_id():
    with Session(engine) as sess:
        output_id = sess.query(Gameweek.gameweek_id, Gameweek.start_date).all()
    return output_id
