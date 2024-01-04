import csv
import json

def convert_to_json(csv_file_path='threatfox_data.csv', json_file_path='threatfox_data.json'):
    data = []
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Data exported to {json_file_path}")
