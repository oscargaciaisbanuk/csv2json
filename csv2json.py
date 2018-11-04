import csv
import json
import argparse

parser = argparse.ArgumentParser(description='Simple CSV to JSON converter')
parser.add_argument("-i", "--input", dest="input", help="csv input file", required=True)
parser.add_argument("-o", "--output", dest="output", help="json output file", required=True)
parser.add_argument("-d", "--delimiter", dest="delimiter", help="Delimiter char", default=",")
args=parser.parse_args()

with open(args.input,  encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=args.delimiter)
    data = list(reader)
    with open(args.output, 'w') as outfile:
        json.dump(data, outfile, indent = 4)
