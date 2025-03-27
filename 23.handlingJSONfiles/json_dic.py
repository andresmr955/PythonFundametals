
import json

new_product = {
    'name': 'Wireless charger JBL',
    'price': 456, 
    'quality': 200, 
    'brand': 'ChargerMasterClass', 
    'category': 'Accessories premium',
    'entry_date': '2024-07-01' 
}

with open('new_json_products.json', mode='r', encoding='utf-8') as file_r:
    file_reader = json.load(file_r)

file_reader.append(new_product)

with open('new_dict_products.json', mode='w', encoding='utf-8') as file_new_w:
    json.dump(file_reader, file_new_w, indent=4)


print("The new product has been added as a dictionary and it was send it as a JSON")