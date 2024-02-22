from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Players(Base):
    __tablename__ = 'players'
    match_id = Column(Integer, ForeignKey('matches.id'), primary_key=True)
    netid = Column(String(10), ForeignKey('users.netid'), primary_key=True)
    match = relationship("Matches", backref="players")
    user = relationship("Users", backref="players")