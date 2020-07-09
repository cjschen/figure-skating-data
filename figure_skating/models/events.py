from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Competition(Base):
    __tablename__ = 'competitions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    level = Column(Integer)
    host_country = Column(String)
    

class IndividualSkate(Base):
    __tablename__ = 'individual_skates'
    id = Column(Integer, primary_key=True, autoincrement=True)
    competition_id = Column(Integer, ForeignKey('competitions.id'))
    athlete_id = Column(Integer, ForeignKey('athletes.id'))
    score = Column(Integer)
    starting_order = Column(Integer)
    rank = Column(Integer)
    
