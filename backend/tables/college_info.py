from sqlalchemy import Column, Integer, String, Float
from database import Base, session

class CollegeInfo(Base):
    __tablename__ = 'college_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    abbreviation = Column(String(3))
    points = Column(Float, default=0.0)