import csv 

original_file = 'products.csv'
new_file_subtotal = 'subtotal_products.csv'

with open(original_file, mode='r') as file_r:
    file_reader = csv.DictReader(file_r)
    subtotal_fieldnames = file_reader.fieldnames + ['subtotal']

    with open(new_file_subtotal, mode='w') as file_w:
        file_writer = csv.DictWriter(file_w, fieldnames=subtotal_fieldnames)
        file_writer.writeheader()

        for row in file_reader:
            row['subtotal'] = float(row['price']) * int(row['quantity'])
            file_writer.writerow(row)