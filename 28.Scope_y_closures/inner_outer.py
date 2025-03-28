x = 'global' #global variable 


#Function extern
def outer_function():
    x = 'enclosing'
    print(f'Here we print x {x} inside outer function')
    #function intern 
    def inner_function(): 
        x = 'local'
        print(f'Here we print x {x} inside inner function')
    inner_function()
    print(f'Here we print x {x} outside inner function but indented')

outer_function()
print(f'Here we print x {x} outside outer function but indented')
