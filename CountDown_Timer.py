import time
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # Define the relationship to TimerSession and Project
    timer_sessions = relationship('TimerSession', back_populates='user')
    projects = relationship('Project', back_populates='user')

class TimerSession(Base):
    __tablename__ = 'timer_sessions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    duration = Column(Integer)

    # Define the relationship to User and Project
    user = relationship('User', back_populates='timer_sessions')
    project = relationship('Project', back_populates='timer_sessions')

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    project_name = Column(String, nullable=False)

    # Define the relationship to User and TimerSession
    user = relationship('User', back_populates='projects')
    timer_sessions = relationship('TimerSession', back_populates='project')

engine = create_engine('sqlite:///mydatabase.db')
Base.metadata.create_all(engine)

def countdown(t, session, user, project=None):
    start_time = datetime.now()
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    end_time = datetime.now()
    duration = (end_time - start_time).seconds

    # Create a new TimerSession entry in the database
    session.add(TimerSession(user=user, project=project, start_time=start_time, end_time=end_time, duration=duration))
    session.commit()

    print('Timer completed!')

def main():
    username = input('Enter your username: ')
    project_name = input('Enter the project name (or press Enter for no project): ')
    t = int(input('Enter the time in seconds: '))

    # Check if the user already exists, or create a new user
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if not user:
        password = input('Create a password: ')
        email = input('Enter your email: ')
        user = User(username=username, password_hash=password, email=email)
        session.add(user)
        session.commit()

    # Check if a project with the given name exists, or create a new project
    project = None
    if project_name:
        existing_project = session.query(Project).filter_by(user=user, project_name=project_name).first()
        if not existing_project:
            project = Project(user=user, project_name=project_name)
            session.add(project)
            session.commit()

    countdown(t, session, user, project)

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    main()
