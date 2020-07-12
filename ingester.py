import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from figure_skating.models import base
from figure_skating.helpers.read_competition import ReadCompetition


data = []

engine = create_engine(os.environ['DATABASE_URL'])
base.Base.metadata.drop_all(engine)
base.Base.metadata.create_all(engine)


Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


filename = 'raw_data/csv/OWG2018_MenSingleSkating_SP_Scores.csv'

with open(filename, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

try: 
    read_competition = ReadCompetition(session)
    read_competition.read_competition(data)
    session.commit()
except:
    session.rollback()
    raise

