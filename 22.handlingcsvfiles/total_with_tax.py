import csv 

original_file = 'tax_subtotal_products.csv'
new_file = 'tax_included_products.csv'

with open(original_file, mode='r') as file_r:
    file_reader = csv.DictReader(file_r)
    file_r_fieldname = file_reader.fieldnames + ['with_tax']

    with open(new_file, mode='w', newline='') as file_w:
        file_writer = csv.DictWriter(file_w, fieldnames=file_r_fieldname)
        file_writer.writeheader()

        for row in file_reader:
            row['with_tax'] = float(row['subtotal']) + float(row['tax'])
            file_writer.writerow(row)