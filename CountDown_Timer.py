from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TimerSession(Base):
    __tablename__ = 'timer_sessions'

    id = Column(Integer, primary_key=True)
    start_time = Column(String)
    end_time = Column(String)
    duration = Column(Integer)

# Create a database engine
engine = create_engine('sqlite:///countdowntimer.db')

# Create the database schema
Base.metadata.create_all(engine)
