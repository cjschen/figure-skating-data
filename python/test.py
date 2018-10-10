# file_str = "c:\Users\Sijia Chen\OneDrive\3B\CS486\Project\raw_data\wc2017_Men_SP_Scores.txt"
from skating import Skater, Skate, Catagory, SkateType, Competition
import unittest

# line = fl.readline().rstrip()
# isInfo = False
# while line:
#     if(line == "Info"):
#         line = fl.readline().rstrip()
#         tokens = line.split(" ")
#         print(line)
#         print("At rank " + tokens[0] + " is " + tokens[1] + " " + tokens[2])
#     line = fl.readline().rstrip()
# fl.close()

# def readProgram(f): 
#     program = []
#     line = readline(f)
#     i = 0
#     summary_line = -1

#     length = len(line)
#     while line[0] != "Deductions":
#         if(line[0] == "Program Components"): 
#             summary_line = i + 1
#         if(line[0] == "Executed"): 
#             summary_line = i - 1
#         program.append(line)
#         line = readline(f)
#         i += 1
#     return program
# def readline(f): 
#     line = f.readline().rstrip().split(',')
#     return line

# def peek_line(f):
#     pos = f.tell()
#     line = f.readline()
#     f.seek(pos)
#     return line

# fl = open("raw_data/wc2017_Men_SP_Scores.csv", 'r') 
fl = open("raw_data/gpcan2017_Men_SP_Scores.csv", 'r') 

gpcan2017_Men_SP = Competition("Grand Prix Skate Canada", Catagory.MEN, SkateType.SP, "")

unosp = Skate(fl)


# gpcan2017_Men_SP.readProgram(fl)

allCompetitions = []
allSkaters = []
# skating.readProgram(fl)