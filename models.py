from sqlalchemy import Column, Integer, Table, String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

# Base is called an Abstract Base Class - Our SQL Alchemy models will inherit from this class
Base = declarative_base()

user_league = Table("user_league",
                    Base.metadata,
                    Column("user_league_id", Integer, primary_key=True),
                    Column("user_id", ForeignKey("user.user_id")),
                    Column("league_id", ForeignKey("league.league_id")),
                    UniqueConstraint("user_id", "league_id")
                    )


class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, unique=False, nullable=False)
    last_name = Column(String, unique=False, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, unique=False, nullable=False)

    leagues = relationship("User",
                           secondary=user_league,
                           order_by="(League.league_id)",
                           backref="users")


class League(Base):
    __tablename__ = "league"
    league_id = Column(Integer, primary_key=True, autoincrement=True)
    start_gameweek = Column(Integer, unique=False, nullable=False)
    league_name = Column(String, unique=False, nullable=False)

    users = relationship("League",
                         secondary=user_league,
                         order_by="(User.user_id)",
                         backref="leagues")


class Team(Base):
    __tablename__ = "team"
    team_id = Column(Integer, primary_key=True, autoincrement=True)
    team_name = Column(String, unique=True, nullable=False)


class Selection(Base):
    __tablename__ = "selection"
    selection_id = Column(Integer, primary_key=True, autoincrement=True)
    gameweek = Column(Integer, unique=False, nullable=False)
    outcome = Column(String, unique=False, nullable=False)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    team_id = Column(Integer, ForeignKey("team.team_id"), nullable=False)
    league_id = Column(Integer, ForeignKey("league.league_id"), nullable=False)


