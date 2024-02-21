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
    winner_id = Column(Integer) # 0 if match is not played yet, -1 if match is a draw
    sport_id = Column(Integer, ForeignKey('sports.id'))
    location = Column(String(20))
    start_time = Column(String(10))
    end_time = Column(String(10))
    date = Column(String(10))
    sport = relationship("Sports", backref="matches")
    college1 = relationship("CollegeInfo", foreign_keys=[college_id1])
    college2 = relationship("CollegeInfo", foreign_keys=[college_id2])

    def __init__(self, college_id1, college_id2, sport_id, location, start_time, end_time, date):
        self.college_id1 = college_id1
        self.college_id2 = college_id2
        self.winner_id = 0
        self.sport_id = sport_id
        self.location = location
        self.start_time = start_time
        self.end_time = end_time
        self.date = date

    def save(self):
        session.add(self)
        session.commit()

    @classmethod
    def update_winner(cls, college_name, match_id):
        match = session.query(cls).filter(cls.id == match_id).first()
        college_id = None
        if college_name != "Draw":
            college_id = CollegeInfo.get_college_id(college_name)
        else:
            college_id = -1
        
        if match and college_id:
            match.winner_id = college_id
            session.commit()
            return True
        else:
            return False
        
    @classmethod
    def get_match(cls, id):
        match = session.query(cls).filter(cls.id == id).first()
        if match:
            return {
                'id': match.id,
                'college_id1': match.college_id1,
                'college_id2': match.college_id2,
                'winner_id': match.winner_id,
                'sport_id': match.sport_id,
                'location': match.location,
                'start_time': match.start_time,
                'end_time': match.end_time,
                'date': match.date
            }
        else:
            return None
        
    @classmethod
    def get_scored_past_matches_for_college(cls, college_name, sport_name=""):
        college_id = CollegeInfo.get_college_id(college_name)
        query = session.query(cls).filter((cls.college_id1 == college_id) | (cls.college_id2 == college_id) & cls.winner_id != 0)
        if sport_name:
            sport_id = Sports.get_sport_id(sport_name)
            query = query.filter(cls.sport_id == sport_id)
        matches = query.all()

        return [{
            'id': match.id,
            'college_id1': match.college_id1,
            'college_id2': match.college_id2,
            'winner_id': match.winner_id,
            'sport_id': match.sport_id,
            'location': match.location,
            'start_time': match.start_time,
            'end_time': match.end_time,
            'date': match.date
        } for match in matches]

        
    @classmethod
    def get_unscored_past_matches_for_college(cls, college_name, sport_name=""):
        date = datetime.now().strftime("%Y-%m-%d")
        time = str(datetime.now().time()).split('.')[0]

        college_id = CollegeInfo.get_college_id(college_name)
        query = session.query(cls).filter((cls.college_id1 == college_id) | (cls.college_id2 == college_id) & cls.winner_id == 0 & cls.date < date & cls.end_time < time)
        if sport_name:
            sport_id = Sports.get_sport_id(sport_name)
            query = query.filter(cls.sport_id == sport_id)
        matches = query.all()

        return [{
            'id': match.id,
            'college_id1': match.college_id1,
            'college_id2': match.college_id2,
            'winner_id': match.winner_id,
            'sport_id': match.sport_id,
            'location': match.location,
            'start_time': match.start_time,
            'end_time': match.end_time,
            'date': match.date
        } for match in matches]
    
    @classmethod
    def get_upcoming_matches_for_college(cls, college_name, sport_name=""):
        date = datetime.now().strftime("%Y-%m-%d")
        time = str(datetime.now().time()).split('.')[0]

        college_id = CollegeInfo.get_college_id(college_name)
        query = session.query(cls).filter((cls.college_id1 == college_id) | (cls.college_id2 == college_id) & (cls.date > date | (cls.date == date & cls.start_time > time))) 
        if sport_name:
            sport_id = Sports.get_sport_id(sport_name)
            query = query.filter(cls.sport_id == sport_id)
        matches = query.all()

        return [{
            'id': match.id,
            'college_id1': match.college_id1,
            'college_id2': match.college_id2,
            'winner_id': match.winner_id,
            'sport_id': match.sport_id,
            'location': match.location,
            'start_time': match.start_time,
            'end_time': match.end_time,
            'date': match.date
        } for match in matches]
    
    @classmethod
    def get_winning_matches_for_college(cls, college_name):
        college_id = CollegeInfo.get_college_id(college_name)
        matches = session.query(cls).filter((cls.college_id1 == college_id) | (cls.college_id2 == college_id) & cls.winner_id == college_id).all()
        if matches:
            return [{
                'id': match.id,
                'college_id1': match.college_id1,
                'college_id2': match.college_id2,
                'winner_id': match.winner_id,
                'sport_id': match.sport_id,
                'location': match.location,
                'start_time': match.start_time,
                'end_time': match.end_time,
                'date': match.date
            } for match in matches]
        else:
            return None
    
    @classmethod
    def get_losing_matches_for_college(cls, college_name):
        college_id = CollegeInfo.get_college_id(college_name)
        matches = session.query(cls).filter((cls.college_id1 == college_id) | (cls.college_id2 == college_id) & cls.winner_id != college_id & cls.winner_id != 0).all()
        if matches:
            return [{
                'id': match.id,
                'college_id1': match.college_id1,
                'college_id2': match.college_id2,
                'winner_id': match.winner_id,
                'sport_id': match.sport_id,
                'location': match.location,
                'start_time': match.start_time,
                'end_time': match.end_time,
                'date': match.date
            } for match in matches]
        else:
            return None
        
    @classmethod
    def get_draw_matches_for_college(cls, college_name):
        college_id = CollegeInfo.get_college_id(college_name)
        matches = session.query(cls).filter((cls.college_id1 == college_id) | (cls.college_id2 == college_id) & cls.winner_id == -1).all()
        if matches:
            return [{
                'id': match.id,
                'college_id1': match.college_id1,
                'college_id2': match.college_id2,
                'winner_id': match.winner_id,
                'sport_id': match.sport_id,
                'location': match.location,
                'start_time': match.start_time,
                'end_time': match.end_time,
                'date': match.date
            } for match in matches]
        else:
            return None
    
