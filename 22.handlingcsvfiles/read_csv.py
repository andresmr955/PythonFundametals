import csv

## read a file
'''

with open('products.csv', mode='r') as file:
    #we want to read this file in a dictionary format
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)
'''


##Show the information by rows
'''

with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f'Producto: {row['name']}, Precio: {row['price']}')


'''

### We add information to the end 

'''
new_product = {
    'name': 'Wireless charger',
    'price': 45, 
    'quality': 100, 
    'brand': 'ChargerMaster', 
    'category': 'Accessories',
    'entry_date': '2024-07-01' 
}

with open('products.csv', mode='a', newline='')as file:
    file.write("\n")
    #we pass the document to the function and is save in out variable 
    csv_writer = csv.DictWriter(file, fieldnames= new_product.keys())
    csv_writer.writerow(new_product)

'''

### A GOOD PRACTICE IS NEVER EDIT THE ORIGINAL FILE RATHER IT IS BETTER TO CREATE A NEW FILE


file_path = 'products.csv'
updated_file_path = 'products_updated.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    #Get the names from the existent rows
    fieldnames_variable = csv_reader.fieldnames + ['total_value']
    
    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames_variable)
        csv_writer.writeheader() ##Write the header
        
        for row in csv_reader:
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csv_writer.writerow(row)