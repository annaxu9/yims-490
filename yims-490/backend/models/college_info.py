from sqlalchemy import Column, Integer, String, Float
from database import Base, session

class CollegeInfo(Base):
    __tablename__ = 'college_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    abbreviation = Column(String(3))
    points = Column(Float, default=0.0)

    def __init__(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation
        self.points = 0

    def save(self):
        session.add(self)
        session.commit()

    @classmethod
    def get_college(cls, name):
        college = session.query(cls).filter_by(name=name).first()
        if college:
            return {
                'name': college.name,
                'abbreviation': college.abbreviation,
                'points': college.points
            }
        else:
            return None
        
    @classmethod
    def get_college_id(cls, name):
        college = session.query(cls).filter_by(name=name).first()
        if college:
            return college.id
        else:
            return None