import re
from enum import Enum, auto
from .common import is_number, stored_score
from ..models.db import DB
from ..models.person import Athlete
from ..models.components import TechnicalElement, PerformanceComponent, Deduction
from ..models.events import Competition, IndividualSkate


class Stage(Enum):
    competition_summary = auto()
    athlete_summary = auto()
    technical = auto()
    performance = auto()
    deduction = auto()

class ReadCompetition():

    def __init__(self):
        self.session = DB.Instance().session

    def read_intro(self, line: list) -> int:

        athlete = self.session.query(Athlete).\
            filter(Athlete.name.like(f"%{line[1].split(' ')[0]}%")).\
            filter(Athlete.name.like(f"%{line[1].split(' ')[1]}%")).\
            one_or_none()
        
        if not athlete:
            athlete = Athlete(name = line[1], country = line[2])

            self.session.add(athlete)
            self.session.flush()

        skate = IndividualSkate(competition_id = self.comp_id,
                                athlete_id = athlete.id,
                                rank=line[0],
                                starting_order = line[3],
                                score=stored_score(line[6]))
        self.session.add(skate)
        self.session.flush()
        return skate.id

    def read_deductions(self, line: list):
        it = iter(line[1:-1])
        # Deductions,Falls:,-1.00(1),-1.00
        for deduction in zip(it, it):
            type = re.sub(r':', '', deduction[0])
            try:
                deduct = Deduction(type=type,
                                    skate_id=self.skate_id,
                                    points=stored_score(deduction[1]))
                self.session.add(deduct)
            except ValueError:
                match = re.search(r'.*?(.*).*', deduction[1])
                num_deducts = int(deduction[1][-2])
                points = stored_score(deduction[1].split('(')[0]) / num_deducts
                for i in range(num_deducts):
                    deduct = Deduction(type=type,
                                        skate_id=self.skate_id,
                                        points=points)
                    self.session.add(deduct)

    def read_technical(self, row: list):
        tech = TechnicalElement(skate_id=self.skate_id,
                                number=row[0],
                                type=re.sub(r'[<*!e>]', '', row[1]),
                                info=row[2],
                                base_score=stored_score(row[3]),
                                highlight_distribution=(row[4] == 'x'),
                                goe=stored_score(row[5]),
                                total_score=stored_score(row[-1]))
        self.session.add(tech)

    def read_performance(self, row: list): 
        perf = PerformanceComponent(skate_id=self.skate_id,
                                    type=row[0],
                                    multiplier=stored_score(row[2]),
                                    total_score=stored_score(row[-1]))
        self.session.add(perf)

    def determine_stage(self, prev_stage, row):
        if prev_stage == None:
            return Stage.competition_summary
        if prev_stage == Stage.competition_summary:
            return Stage.athlete_summary
        if prev_stage == Stage.athlete_summary or prev_stage == Stage.technical and is_number(row[0]):
            return Stage.technical
        if prev_stage == Stage.technical and not is_number(row[0]):
            return Stage.performance
        if prev_stage == Stage.performance and  row[0] != "Deductions":
            return Stage.performance
        if prev_stage == Stage.performance and row[0] == "Deductions":
            return Stage.deduction
        if prev_stage == Stage.deduction:
            return Stage.athlete_summary
        raise "Unknown Stage combination"
    def add_competition(self, line, filename):

        attr = filename.split('_')
        comp = Competition(level = 1,
                           type=attr[0],
                           host_country=line[0],
                           city=line[1],
                           season=attr[1],
                           sp_file_name=filename)

        self.session.add(comp)
        self.session.flush()
        return comp.id
        

    def read_competition(self, data, filename):
        
        stage = None
        self.skate_id = None

        for row in data: 
            stage = self.determine_stage(stage, row)

            if stage == Stage.competition_summary:
                self.comp_id = self.add_competition(row, filename)
            elif stage == Stage.athlete_summary: 
                # Metadata. Always one row
                self.skate_id = self.read_intro(row)
            elif stage == Stage.technical:
                # TES
                if is_number(row[2]):
                # No notes on athlete, but we want data to be consistent
                    row.insert(2, '')
                    print(row)
                self.read_technical(row)
            elif stage == Stage.performance:
                # PCS
                # ['Performance', '1.00', '6.75', '7.75', '7.00', '7.25', '6.75', '7.50', '8.00', '6.50', '6.75', '7.11']
                self.read_performance(row)
            elif stage == Stage.deduction:
                # Deductions
                self.read_deductions(row)

    def reformat_competition(self, data):
        for row in data: 
            if stage == Stage.technical:
                # TES
                if is_number(row[2]):
                    row.insert(2, '')
                    print(row)
                read_technical(row)
            elif stage == 2:
                # PCS
                # ['Performance', '1.00', '6.75', '7.75', '7.00', '7.25', '6.75', '7.50', '8.00', '6.50', '6.75', '7.11']
                self.read_performance(row)
            elif stage == 3:
                # Deductions
                self.read_deductions(row)
                stage = 0
        return data