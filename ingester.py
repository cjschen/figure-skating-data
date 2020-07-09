import csv
import os
import re
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from figure_skating.models import base
from figure_skating.models.person import Athlete
from figure_skating.models.components import TechnicalElement, PerformanceComponent, Deduction
from figure_skating.models.events import Competition, IndividualSkate


def is_number(num: str) -> bool: 
    try:
        float(num)
        return True
    except ValueError:
        return False      

def read_intro(line: list):
    pass

def read_deduction(line: list):
    
    pass

def read_tes(line: list):
    pass


def read_pcs(line: list):
    pass

def stored_score(str: float):
    return int(float(str) * 100)



data = []

engine = create_engine(os.environ['DATABASE_URL'])
base.Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


filename = 'raw_data/csv/OWG2018_MenSingleSkating_SP_Scores.csv'

with open(filename, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

    athletes = []
    athlete = {}
    stage = 0

comp = Competition(level = 1, host_country = 'KOR')
session.add(comp)
skate_identifier = None

for row in data: 
    print(row)
    # New athlete, push previous athlete onto list 
    if row[0] == "Deductions": 
        stage = 3
    if stage == 1 and not is_number(row[0]):
        stage = 2
    if stage == 0: 
        # Metadata. Always one row

        athlete = Athlete(name = row[1], country = row[2])
        session.add(athlete)
        session.commit()
        skate = IndividualSkate(competition_id = comp.id,
                                athlete_id = athlete.id,
                                rank=row[0],
                                starting_order = row[3],
                                score=stored_score(row[6]))
        session.add(skate)
        session.commit()

        skate_identifier = skate.id
        stage = stage + 1
        continue
    elif stage == 1:
        # TES

        if is_number(row[2]):
        # No notes on athlete, but we want data to be consistent
            row.insert(2, '')
            print(row)
        # ['1', '4T<<+COMBO', '<<', '4.30', '', '-2.10', '-3', '-3', '-3', '-3', '-3', '-3', '-3', '-3', '-3', '2.20']
        
        tech = TechnicalElement(skate_id=skate_identifier,
                                number=row[0],
                                type=re.sub(r'[<*!e>]', '', row[1]),
                                info=row[2],
                                base_score=stored_score(row[3]),
                                highlight_distribution=(row[4] == 'x'),
                                goe=stored_score(row[5]),
                                total_score=stored_score(row[-1]))
        session.add(tech)
    elif stage == 2:
        # PCS
        # ['Performance', '1.00', '6.75', '7.75', '7.00', '7.25', '6.75', '7.50', '8.00', '6.50', '6.75', '7.11']
        perf = PerformanceComponent(skate_id=skate_identifier,
                                    type=row[0],
                                    multiplier=stored_score(row[2]),
                                    total_score=stored_score(row[-1]))
        session.add(perf)
    elif stage == 3:
        # Deductions
        it = iter(row[1:-1])
        # Deductions,Falls:,-1.00(1),-1.00
        for deduction in zip(it, it):
            type = re.sub(r':', '', deduction[0])
            try:
                deduct = Deduction(type=type,
                                   skate_id=skate_identifier,
                                   points=stored_score(deduction[1]))
                session.add(deduct)
            except ValueError:
                match = re.search(r'.*?(.*).*', deduction[1])
                num_deducts = int(deduction[1][-2])
                points = stored_score(deduction[1].split('(')[0]) / num_deducts
                for i in range(num_deducts):
                    deduct = Deduction(type=type,
                                       skate_id=skate_identifier,
                                       points=points)
                    session.add(deduct)


        athletes += [athlete]
        athlete = {}
        stage = 0
session.commit()
