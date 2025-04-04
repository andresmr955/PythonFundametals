x = 5
y = 9
print(id(x))
print(id(y))

def modify_global():
    ##This line makes reference to say to the function that x is not local is global
    global x 
    y = 16
    print(id(y))
    print(id(x))

    x+=3
    print(f'Value modified: {x}')

modify_global()
print(x)