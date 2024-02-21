from sqlalchemy import Column, Integer, String
from database import Base, session

class Sports(Base):
    __tablename__ = 'sports'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    points_for_win = Column(Integer)
    season = Column(String(20))
    icon = Column(String(20))

    def __init__(self, name, points_for_win, season, icon):
        self.name = name
        self.points_for_win = points_for_win
        self.season = season
        self.icon = icon

    def save(self):
        session.add(self)
        session.commit()

    @classmethod
    def get_sport_by_name(cls, name):
        sport = session.query(cls).filter(cls.name == name).first()
        if sport:
            return {
                'name': sport.name,
                'points_for_win': sport.points_for_win,
                'season': sport.season,
                'icon': sport.icon
            } 
        else:
            return None
    
    @classmethod
    def get_sport_id(cls, name):
        sport = session.query(cls).filter(cls.name == name).first()
        if sport:
            return sport.id
        else:
            return None
    