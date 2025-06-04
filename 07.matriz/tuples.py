my_tuple = (1, 'two', True)
print(my_tuple[2])

## We have to create a new tuple to change the value of a tuple

##This is not the same 
#<class 'int'>
#<class 'tuple'>
exam1 = (1)
print(type(exam1))
tuple1 = (1,)
print(type(tuple1))


# we can reasign the value of a tuple
tuple1 = (1,)
my_other_tuple = (2,4,5,6)

tuple1 += my_other_tuple
print(tuple1)

# we can unpack a tuple
a, b, c, d = my_other_tuple
print(a, b, c, d)

# tuple with a function

def coordinates():
    return (5, 4)
 
coordinates = coordinates()

print(coordinates)

x, y = coordinates
print(x, y)