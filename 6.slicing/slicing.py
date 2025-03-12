a = [1,2,3,4,5]
b = a 

print(f'Esta es la lista a => {a}')
print(f'Esta es la lista :b => {b}')
#To delete an element from the array

del a[0]
#To know its id
print(id(a))
print(id(b))
#change the object in memory

c = a[:]
print(f'Esta es la lista :a => {c}')
print(id(c))
