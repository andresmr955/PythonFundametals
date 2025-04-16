 

def my_map(list, func):
  # Tu código aquí 👈
  
  return [func(i) for i in list]

print(my_map([1, 2, 3, 4], lambda num: num * 2))
