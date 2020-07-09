from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .base import Base

class Deduction(Base):
    __tablename__ = 'deductions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    skate_id = Column(Integer, ForeignKey('individual_skates.id'))
    type = Column(String)
    points = Column(Integer)
    def __repr__(self):
        return f'Deduction({self.id}: {self.type}, -{self.points})'
        # return 'Deduction({self.id}: {self.type}, -{self.points})'


# ['1', '4T<<+COMBO', '<<', '4.30', '', '-2.10', '-3', '-3', '-3', '-3', '-3', '-3', '-3', '-3', '-3', '2.20']
class TechnicalElement(Base):
    __tablename__ = 'technical_elements'
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer)
    skate_id = Column(Integer, ForeignKey('individual_skates.id'))
    type = Column(String)
    base_score = Column(Integer)
    goe = Column(Integer)
    highlight_distribution = Column(Boolean)
    total_score = Column(Integer)
    info = Column(String)

class PerformanceComponent(Base):
    __tablename__ = 'performance_components'
    id = Column(Integer, primary_key=True, autoincrement=True)
    skate_id = Column(Integer, ForeignKey('individual_skates.id'))
    type = Column(String)
    multiplier = Column(Integer)
    total_score = Column(Integer)




