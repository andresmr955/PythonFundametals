x = 5
y = 9
print(id(x), x)
print(id(y), y)

def modify_global():
    ##This line makes reference to say to the function that x is not local is global
    global x 
    y = 16
    print(id(y), y)
    print(id(x), x)

    x+=3
    print(f'Value modified: {x} x')

modify_global()
print(x)