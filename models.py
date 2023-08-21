from sqlalchemy import Column, Integer, Table, String, UniqueConstraint, ForeignKey, Date, Time, DateTime
from sqlalchemy.orm import relationship, declarative_base, validates
import re

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

    @validates("email_address")
    def validate_email(self, key, address):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(pattern, address):
            raise ValueError("Invalid email address")
        if key != "email_address":
            raise ValueError("Key must be 'email'")
        return address

    @validates("password")
    def validate_password(self, key, password):
        pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        if not re.fullmatch(pattern, password):
            raise ValueError("Invalid password")
        if key != "password":
            raise ValueError("Key must be 'password'")
        return password


class League(Base):
    __tablename__ = "league"
    league_id = Column(Integer, primary_key=True, autoincrement=True)
    gameweek_id = Column(Integer, ForeignKey("gameweek.gameweek_id"), nullable=False)
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
    gameweek_id = Column(Integer, ForeignKey("gameweek.gameweek_id"), nullable=False)
    outcome = Column(String, unique=False, nullable=False)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    team_id = Column(Integer, ForeignKey("team.team_id"), nullable=False)
    league_id = Column(Integer, ForeignKey("league.league_id"), nullable=False)


class Gameweek(Base):
    __tablename__ = "gameweek"
    gameweek_id = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(Date, unique=False, nullable=False)
    start_time = Column(Time, unique=False, nullable=False)
    end_date = Column(Date, unique=False, nullable=False)
    end_time = Column(Time, unique=False, nullable=False)
