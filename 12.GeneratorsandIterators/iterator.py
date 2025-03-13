#  iterador's example

#Create a list
my_list = [1,2,3,4]

#Get one list
my_iter= iter(my_list)

#Use the iterator
print(next(my_iter)) 
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#STRING ITERATORS

text = "Hola mundo"

iter_text = iter(text)

#Using loop
for char in iter_text:
    print(f'This is the loop {char}')

#Create an iterator to impair numbers

#Limit
limit = 10

odd_itter = iter(range(1,limit + 1, 2))

#Use iterator

for num in odd_itter:
    print(num)