import csv
import json
import pandas as pd

def json_to_csv(file_path):
    
    new_path = file_path+'.json'

    with open(file_path,'r', encoding='utf-8') as f:
        data = json.loads(f.read())

    df = pd.json_normalize(data)

    df.to_csv(new_path, index=False, encoding='utf-8')
        
    return new_path

def csv_to_json(file_path):
    
    new_path = file_path+'.json'
    
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    with open(new_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2, ensure_ascii=False)
        
    return new_path