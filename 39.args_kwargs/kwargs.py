def print_info(**kwargs):
   for key, value in kwargs.items():
      print(f'{key}: {value}') 

print_info(name='Carlos', age=30, city='Bogota')
print_info(name='Carlos', age=30, city='Bogota', country="Colombia")