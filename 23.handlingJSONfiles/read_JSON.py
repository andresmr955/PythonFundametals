'''
import json 

##Read file
with open('products.json', mode='r') as file:
    products = json.load(file)

#Show content

    for product in products:
        ##print(product) Print products in dictionary
        print(f'Product: {product['name']}, Price {product['price']}')

'''

import json

current_file ='products.json'
new_file = 'new_products.json'

new_product = {
    'name': 'Wireless charger Andres',
    'price': 45, 
    'quality': 100, 
    'brand': 'ChargerMaster', 
    'category': 'Accessories',
    'entry_date': '2024-07-01' 
}

with open(current_file, mode='r') as file:
    file_reader = json.load(file)
    
file_reader.append(new_product)

with open(new_file, mode='w') as file_w:
    json.dump(file_reader, file_w, indent=4)