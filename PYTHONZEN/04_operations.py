set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

set_c = set_a.union(set_b)
print(f'Union: => {set_c}')   

print(f'Union with operator | : => {set_a | set_b}')

set_c = set_a.intersection(set_b)
print(f'Interesection: => {set_c}')

print(f'Intersection with &: =>  {set_a & set_b}') 

set_d = set_a.difference(set_b)
print(f'Difference: {set_d}')
print(f'Difference with - {set_a - set_b}')

set_si = set_a.symmetric_difference(set_b)
print(f'Symmeytric difference: {set_si}')
print(f'Symmetric difference with  ^ : => {set_a ^ set_b}')
