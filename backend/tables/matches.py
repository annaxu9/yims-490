from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base, session
from sqlalchemy.orm import relationship
from .college_info import CollegeInfo
from .sports import Sports
from datetime import datetime

class Matches(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True, autoincrement=True)
    college_id1 = Column(Integer, ForeignKey('college_info.id'))
    college_id2 = Column(Integer, ForeignKey('college_info.id'))
    college_pts1 = Column(Integer, default=-1)
    college_pts2 = Column(Integer, default=-1)
    sport_id = Column(Integer, ForeignKey('sports.id'))
    location = Column(String(20))
    date = Column(String(10))
    start_time = Column(String(10))
    sport = relationship("Sports", backref="matches")
    college1 = relationship("CollegeInfo", foreign_keys=[college_id1])
    college2 = relationship("CollegeInfo", foreign_keys=[college_id2])

