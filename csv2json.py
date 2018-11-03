import csv
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", help="csv input file")
parser.add_argument("output", help="json output file")
args=parser.parse_args()

with open(args.input,  encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=";")
    data = list(reader)
    with open(args.output, 'w') as outfile:
        json.dump(data, outfile, indent = 4)
