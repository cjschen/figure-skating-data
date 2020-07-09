from sqlalchemy import Column, Integer, String, DateTime
from .base import Base

class Athlete(Base):
    __tablename__ = 'athletes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    birthday = Column(DateTime)
    country = Column(String)
    

# class Judge(Base):
#     __tablename__ = 'judges'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String)
#     country = Column(String)

