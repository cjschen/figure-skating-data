from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Competition(Base):
    __tablename__ = 'competitions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    level = Column(Integer, nullable=False)
    host_country = Column(String, nullable=False)
    

class IndividualSkate(Base):
    __tablename__ = 'individual_skates'
    id = Column(Integer, primary_key=True, autoincrement=True)
    competition_id = Column(Integer, ForeignKey('competitions.id'), nullable=False)
    athlete_id = Column(Integer, ForeignKey('athletes.id'), nullable=False)
    score = Column(Integer, nullable=False)
    starting_order = Column(Integer, nullable=False)
    rank = Column(Integer, nullable=False)
    
