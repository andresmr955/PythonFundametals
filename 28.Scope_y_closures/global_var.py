x = 5

def modify_global():
    ##This line makes reference to say to the function that x is not local is global
    global x 
    x+=3
    print(f'Value modified: {x}')

modify_global()
print(x)