from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import League, Team, User, Gameweek

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

#gameweek = [Gameweek(start_date=, start_time=15.21, end_date=13 / 5 / 2023, end_time=12.21),
            #Gameweek(start_date=20 / 6 / 2023, start_time=13.00, end_date=21 / 5 / 2023, end_time=13.00)]

leagues = [League(gameweek_id=1, league_name="The best league"),
           League(gameweek_id=2, league_name="Tottenham Fans")]

engine = create_engine("sqlite:///fantasy_football.db", echo=True)

with Session(engine) as sess:
    # sess.add_all(users)
    # sess.add_all(teams)
    # sess.add_all(leagues)
    #sess.add_all(gameweek)
    sess.commit()

# leagues[0].users.append(users[0])
# leagues[0].users.append(users[2])
# leagues[1].users.append(users[1])
# leagues[1].users.append(users[2])
