from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import League, Team, User, Gameweek
from datetime import datetime

teams = [Team(team_name="Arsenal"),
         Team(team_name="Aston Villa"),
         Team(team_name="Bournemouth"),
         Team(team_name="Brentford"),
         Team(team_name="Brighton & Hove Albion"),
         Team(team_name="Burnley"),
         Team(team_name="Chelsea"),
         Team(team_name="Crystal Palace"),
         Team(team_name="Everton"),
         Team(team_name="Fulham"),
         Team(team_name="Liverpool"),
         Team(team_name="Luton Town"),
         Team(team_name="Manchester City"),
         Team(team_name="Manchester United"),
         Team(team_name="Newcastle United"),
         Team(team_name="Nottingham Forest"),
         Team(team_name="Sheffield United"),
         Team(team_name="Tottenham Hotspur"),
         Team(team_name="West Ham United"),
         Team(team_name="Wolverhampton Wanderers")]

users = [User(first_name="Toby", last_name="Willmott", username="tobywillmott", password="P@ssword123"),
         User(first_name="James", last_name="Smith", username="jamessmith", password="p@rdhE123"),
         User(first_name="John", last_name="Dixon", username="tomdixon", password="Th@$$or99od"), ]

gameweek = [Gameweek(start_date=datetime(2023, 8, 11, 17, 30, 0)),
            Gameweek(start_date=datetime(2023, 8, 19, 12, 30, 0)),
            Gameweek(start_date=datetime(2023, 8, 26, 12, 30, 0)),
            Gameweek(start_date=datetime(2023, 9, 2, 12, 30, 0)),
            Gameweek(start_date=datetime(2023, 9, 16, 12, 30, 0)),
            Gameweek(start_date=datetime(2023, 9, 23, 12, 30, 0)),
            Gameweek(start_date=datetime(2023, 9, 30, 12, 30, 0)),
            Gameweek(start_date=datetime(2023, 10, 7, 12, 30, 0)),
            Gameweek(start_date=datetime(2023, 10, 21, 12, 30, 0)),
            Gameweek(start_date=datetime(2023, 10, 28, 12, 30, 0)),
            Gameweek(start_date=datetime(2023, 11, 4, 12, 30, 0)),
            Gameweek(start_date=datetime(2023, 11, 11, 12, 30, 0)),
            Gameweek(start_date=datetime(2023, 11, 25, 12, 30, 0)),
            Gameweek(start_date=datetime(2023, 12, 2, 12, 30, 0)),
            Gameweek(start_date=datetime(2023, 12, 5, 12, 30, 0)),
            Gameweek(start_date=datetime(2023, 12, 9, 12, 30, 0)),
            Gameweek(start_date=datetime(2023, 12, 16, 12, 30, 0)),
            Gameweek(start_date=datetime(2023, 12, 23, 12, 30, 0)),
            Gameweek(start_date=datetime(2023, 12, 26, 12, 30, 0)),
            Gameweek(start_date=datetime(2023, 12, 30, 12, 30, 0)),
            Gameweek(start_date=datetime(2024, 1, 13, 12, 30, 0)),
            Gameweek(start_date=datetime(2024, 1, 30, 17, 15, 0)),
            Gameweek(start_date=datetime(2024, 2, 3, 12, 30, 0)),
            Gameweek(start_date=datetime(2024, 2, 10, 12, 30, 0)),
            Gameweek(start_date=datetime(2024, 2, 17, 12, 30, 0)),
            Gameweek(start_date=datetime(2024, 2, 24, 12, 30, 0)),
            Gameweek(start_date=datetime(2024, 3, 2, 12, 30, 0)),
            Gameweek(start_date=datetime(2024, 3, 9, 12, 30, 0)),
            Gameweek(start_date=datetime(2024, 3, 16, 12, 30, 0)),
            Gameweek(start_date=datetime(2024, 3, 30, 12, 30, 0)),
            Gameweek(start_date=datetime(2024, 4, 2, 17, 15, 0)),
            Gameweek(start_date=datetime(2024, 4, 6, 12, 30, 0)),
            Gameweek(start_date=datetime(2024, 4, 13, 12, 30, 0)),
            Gameweek(start_date=datetime(2024, 4, 20, 12, 30, 0)),
            Gameweek(start_date=datetime(2024, 4, 27, 12, 30, 0)),
            Gameweek(start_date=datetime(2024, 5, 4, 12, 30, 0)),
            Gameweek(start_date=datetime(2024, 5, 11, 12, 30, 0)),
            Gameweek(start_date=datetime(2024, 5, 19, 13, 30, 0))]

leagues = [League(gameweek_id=1, league_name="The best league"),
           League(gameweek_id=2, league_name="Tottenham Fans")]


engine = create_engine("sqlite:///fantasy_football.db", echo=True)

with Session(engine) as sess:
    sess.add_all(users)
    sess.add_all(teams)
    sess.add_all(leagues)
    sess.add_all(gameweek)
    sess.commit()


