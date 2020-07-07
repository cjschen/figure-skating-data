import csv 

def is_number(num: str) -> bool: 
    try:
        float(num)
        return True
    except ValueError:
        return False      

data = []

filename = 'raw_data/csvs/OWG2018_MenSingleSkating_SP_Scores.csv'

with open(filename, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

    skaters = []
    skater = {}
    stage = 0

    for row in data: 
        print(row)
        # New skater, push previous skater onto list 
        if row[0] == "Deductions": 
            stage = 3
        if stage == 1 and not is_number(row[0]):
            stage = 2
        if stage == 0: 
            # Metadata. Always one row
            skater['rank'] = row[0]
            skater['name'] = row[1]
            skater['country'] = row[2]
            skater['starting_order'] = row[3]
            stage = stage + 1
            continue
        elif stage == 1:
            # TES

            if is_number(row[2]):
            # No notes on skater, but we want data to be consistent
                row.insert(2, '')
                print(row)
            row[1]
        elif stage == 2:
            # PCS
            continue
        elif stage == 3:
            # Deductions
            skaters += [skater]
            skater = {}
            stage = 0


with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)