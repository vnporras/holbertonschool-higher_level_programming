import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

            if not data:
                return False

            json_filename = 'data.json'
            with open(json_filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            return True

    except FileNotFoundError:
        return False
