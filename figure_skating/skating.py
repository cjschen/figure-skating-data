from enum import Enum, auto
from abc import ABCMeta
import pickle
import re
import json
glossary = {}

with open("glossary.json", 'r') as f:
    glossary = json.loads(f.read())
assert(glossary != {})

all_athletes = []
all_competitions = []

class Catagory(Enum):
    MEN = 1
    LADIES = 2

class SkateType(Enum):
    SP = auto()
    FS = auto()

class DeductionTypes(Enum):
    Fall = auto()
class Deduction:


class Competition: 
    def __init__(self, name, catagory, skate_type, date, skates = []): 
        self.name = name 
        self.skates = skates
        self.date = date
        self.skate_type = skate_type
        self.catagory = catagory



class Athlete():
    def __init__(self, name, catagory, skates = []): 
        self.name = name
        self.catagory = catagory
        self.file_name = name.lower().replace(" ", "_") + ".txt"
        self.skates = skates

    def get_file_name(self): 
        return self.name.replace(" ", "_").lower() + '.pk1'
    
    def save(self):
        with open(self.get_file_name(), 'wb') as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)

    def addSkate(self, skate):
        if(skate not in self.skates):
            self.skates.append(skate)

class Skate(): 
    def __init__(self, f):

        self.TES = 0
        self.PCS = 0
        program = []
        line = readline(f)
        i = 0
        summary_line = -1
        technical_line = -1
        technical_end = -1
        performance_line = -1
        

        length = len(line)
        while line[0] != "Deductions":
            if(line[0] == "Program Components"): 
                performance_line = i + 1
                technical_end = i - 1
            if(line[0] == "Executed"): 
                summary_line = i - 1
                technical_line = i + 2
            program.append(line)

            line = readline(f)
            i += 1
        
        athlete_name = program[summary_line][0].split('_', 1)
        athlete_name.pop(0)
        athlete_name = "".join(athlete_name)
        self.athlete = None
        for x in all_athletes:
            if x.name == athlete_name:
                self.athlete = x
                break
        if(self.athlete is None): 
            self.athlete = Athlete(athlete_name, Catagory.MEN)
        
        self.athlete.addSkate(self)
        self.elements = []
        self.performances = []

        line = program[technical_line]
        
        for i in range(technical_line, technical_end): 
            self.elements.append(Element(program[i]))

        for i in range(performance_line, performance_line + 5): 
            self.performances.append(program[i][length - 1])
    # def __init__(self, competition, athlete, type, elements = []):
    #     self.athlete = athlete
    #     athlete.addSkate(self)
    #     self.TES = 0
    #     self.PCS = 0
    #     self.elements = elements

"3 StSq3,3.30,,,1.14,2 3,1 2,1,3 3,2 3,4.44"
"5 3F+3T,10.56,,x 1.30,1 2,2 2,2,2 2,1 2,11.86"
class Element(): 
    def __init__(self, line): 
        # self.competition = competition
        length = len(line)

        self.take_notes(line[1])
        self.base = float(self.removeExtra(line[1]))
        self.goe = float(self.removeExtra(line[2]))
        self.score = line[length - 1]
        self.notes = line[1]
        self.attributes = []

    def removeExtra(self, st):
        st.replace("<", "").replace(" ", "").replace(">", "").replace("!", "").replace("e", "")
        st = st.split("V")[0]
        return st
    def take_notes(self, st):
        attributes = glossary["technical_elements"]["jumps"]['attributes']
        for item in attributes: 
            if item[0] in st: 
                self.attributes += item[1]
def readline(f): 
    line = f.readline().rstrip().split(',')
    return line
