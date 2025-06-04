import csv 

original_file = 'subtotal_products.csv'
modified_file_tax = 'tax_subtotal_products.csv'

with open(original_file, mode='r') as file_r:
    file_reader = csv.DictReader(file_r)
    file_r_fieldname = file_reader.fieldnames + ['tax']

    with open(modified_file_tax, mode='w', newline='') as file_w:
        file_writer = csv.DictWriter(file_w, fieldnames=file_r_fieldname)
        file_writer.writeheader()

        for row in file_reader:
            row['tax'] = float(row['subtotal']) * 0.10
            file_writer.writerow(row)
        
