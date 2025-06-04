set_countries = {"Colombia", "Mexico", "Bolivia","Colombia"} 

size = len(set_countries)
print(size)

print('Colombia' in set_countries)
print("Peru" in set_countries)


# add 
set_countries.add('Peru')
print(set_countries)
set_countries.add('Peru')
print(set_countries)

#update
set_countries.update({'argentina', 'ecu', 'peru'})
print(set_countries)

## Remove
set_countries.remove('Colombia')
print(set_countries)


set_countries.remove('Colom')
print(set_countries)

# try to remove without crash

set_countries.discard('ar')
print(set_countries)

set_countries.add("Brazil")

