import csv
import os
from figure_skating.helpers.read_competition import ReadCompetition
from shutil import copyfile

data = []

for filename in os.listdir('raw_data/csv'):
    data = []
    with open(f"raw_data/csv/{filename}", newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

        read_competition = ReadCompetition()
        data = read_competition.reformat_competition(data)

    # copyfile(f"raw_data/csv/{filename}", f"raw_data/csv/{filename}.bak")
    with open(f"raw_data/csv/{filename}", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
