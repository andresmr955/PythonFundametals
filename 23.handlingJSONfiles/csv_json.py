import csv
import json

original_file = 'products.csv'
new_file = 'json_csv_converted.json'

with open(original_file, mode='r', encoding='utf-8')as file_r:
    file_reader = csv.DictReader(file_r)
    data = list(file_reader)

json_data = json.dumps(data, indent=4)

with open(new_file, mode='w', encoding='utf-8') as file_w:
    file_w.write(json_data)

print("CSV document was already converted to JSON")