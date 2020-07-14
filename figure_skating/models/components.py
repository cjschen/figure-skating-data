from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .base import Base

class Deduction(Base):
    __tablename__ = 'deductions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    skate_id = Column(Integer, ForeignKey('individual_skates.id'), nullable=False)
    type = Column(String, nullable=False)
    points = Column(Integer, nullable=False)
    def __repr__(self):
        return f'Deduction({self.id}: {self.type}, -{self.points})'
        # return 'Deduction({self.id}: {self.type}, -{self.points})'


# ['1', '4T<<+COMBO', '<<', '4.30', '', '-2.10', '-3', '-3', '-3', '-3', '-3', '-3', '-3', '-3', '-3', '2.20']
class TechnicalElement(Base):
    __tablename__ = 'technical_elements'
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer, nullable=False)
    skate_id = Column(Integer, ForeignKey('individual_skates.id'), nullable=False)
    type = Column(String, nullable=False)
    base_score = Column(Integer, nullable=False)
    goe = Column(Integer, nullable=False)
    highlight_distribution = Column(Boolean, nullable=False)
    total_score = Column(Integer, nullable=False)
    info = Column(String, nullable=False)

class PerformanceComponent(Base):
    __tablename__ = 'performance_components'
    id = Column(Integer, primary_key=True, autoincrement=True)
    skate_id = Column(Integer, ForeignKey('individual_skates.id'), nullable=False)
    type = Column(String, nullable=False)
    multiplier = Column(Integer, nullable=False)
    total_score = Column(Integer, nullable=False)




