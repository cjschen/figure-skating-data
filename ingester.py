import csv
import os
from figure_skating.helpers.read_competition import ReadCompetition
from figure_skating.models.db import DB

data = []

session = DB.Instance().session

for filename in os.listdir('raw_data/csv'):
    with open(f"raw_data/csv/{filename}", newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    try: 
        read_competition = ReadCompetition()
        read_competition.read_competition(data, filename)
        session.commit()
    except:
        session.rollback()
        raise

