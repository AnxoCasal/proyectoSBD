import csv
import json
import pandas as pd

def json_to_csv(json_file):

    with open(json_file,'r', encoding='utf-8') as f:
        data = json.loads(f.read())

    df = pd.json_normalize(data)

    df.to_csv('output.csv', index=False, encoding='utf-8')

def csv_to_json(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    with open('output.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2, ensure_ascii=False)