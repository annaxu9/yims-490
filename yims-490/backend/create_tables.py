from database import engine, Base
from models import CollegeInfo, Sports, Users, Matches, Players

# Drop all tables in the engine.
Base.metadata.drop_all(engine)

# Create all tables in the engine. 
Base.metadata.create_all(engine)
