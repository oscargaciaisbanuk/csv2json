import csv
import json

with open("testdata/23_Time_Card.csv",  encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=";")
    data = list(reader)
    with open('target/data.json', 'w') as outfile:
        json.dump(data, outfile, indent = 4)
