import csv

def read_csv(path):
   # Tu código aquí 👇
    total = 0
    fieldnames = ['name_area', 'expenses']

    with open(path, mode='r') as file:
        file_reader = csv.DictReader(file, fieldnames=fieldnames)

        for item in file_reader:
            total += int(item['expenses'])
    
    
    return total

response = read_csv('./data.csv')
print(response)