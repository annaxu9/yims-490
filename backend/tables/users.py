from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base, session
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = 'users'
    netid = Column(String(10), primary_key=True)
    firstname = Column(String(20))
    lastname = Column(String(20))
    college_id = Column(Integer, ForeignKey('college_info.id'))
    role = Column(String(10)) # role can be 'player', 'admin', 'ref'
    points = Column(Integer, default=0)
    college = relationship("CollegeInfo", backref="users")

