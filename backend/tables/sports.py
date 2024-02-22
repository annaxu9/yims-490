from sqlalchemy import Column, Integer, String
from database import Base, session

class Sports(Base):
    __tablename__ = 'sports'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    points_for_win = Column(Integer)
    season = Column(String(20))
    icon = Column(String(20))
    