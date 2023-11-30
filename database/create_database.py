from sqlalchemy import create_engine
from models import Base

engine = create_engine("sqlite:///fantasy_football.sqlite", echo=True)
Base.metadata.create_all(engine)