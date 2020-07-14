from sqlalchemy import Column, Integer, String, DateTime
from .base import Base

class Athlete(Base):
    __tablename__ = 'athletes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    birthday = Column(DateTime)
    country = Column(String, nullable=False)
    

# class Judge(Base):
#     __tablename__ = 'judges'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String)
#     country = Column(String)

