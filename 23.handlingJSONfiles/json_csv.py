import csv
import json

with open('new_dict_products.json', mode='r', encoding='utf-8') as file_r:
    file_reader = json.load(file_r)

var_fieldnames = set()

for item in file_reader:
    var_fieldnames.update(item.keys())

var_fieldnames = list(var_fieldnames)

with open('new_products_dict_csv.csv', mode='w', encoding='utf-8', newline='') as file_w:
    
    file_writer = csv.DictWriter(file_w, fieldnames=var_fieldnames)

    file_writer.writeheader()

    file_writer.writerows(file_reader)

    print("We have done the exercise")