from collections import Counter

ex_packages =[
  (1, 20, "Mexico"),
  (2, 15.5, "Colombia"),
  (3, 30, "Mexico"),
  (4, 12, "Argentina"),
  (5, 8.2, "Colombia"),
  (6, 25, "Mexico"),
  (7, 18.7, "Argentina"),
  (8, 5, "Colombia"),
  (9, 22.3, "Argentina"),
  (10, 14.8, "Colombia")
]

def get_packages_info(packages):
   # Tu código aquí 👈
   list_weight  = [weight[1] for weight in packages]
   total_weight = sum(list_weight)
   total_weight = round(total_weight, 2)
   dict_global = {}
   dict_global["total_weight"] = total_weight
   all_countries = []

   all_countries = tuple(values [2] for values in packages)

    
   destinations = {destino: all_countries.count(destino) for destino in all_countries}

   dict_global["destinations"] = destinations
   
   return dict_global


print(get_packages_info(ex_packages))