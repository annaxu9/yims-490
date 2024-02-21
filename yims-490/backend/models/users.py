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

    def __init__(self, netid, firstname, lastname, college_id, role):
        self.netid = netid
        self.firstname = firstname
        self.lastname = lastname
        self.college_id = college_id
        self.role = role
        self.points = 0
    
    def save(self):
        session.add(self)
        session.commit()

    @classmethod
    def get_user(cls, netid):
        user = session.query(cls).filter(cls.netid == netid).first()
        if user:
            return {
                'netid': user.netid,
                'firstname': user.firstname,
                'lastname': user.lastname,
                'college_id': user.college_id,
                'role': user.role,
                'points': user.points
            }
        else:
            return None
    
