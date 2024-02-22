from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import College

# Create an engine that connects to the MySQL database
engine = create_engine("mysql+mysqlconnector://root:Tiantian9!@localhost/yims")

# Create a sessionmaker factory bound to the engine
Session = sessionmaker(bind=engine)

# Create a new session
session = Session()

# Base class for declarative models
Base = declarative_base()

# add a college
def add_college(college):
    session.add(college)
    session.commit()
