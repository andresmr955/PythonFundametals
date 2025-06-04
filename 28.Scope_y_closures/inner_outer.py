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


def make_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = make_adder(10)  # `add_10` es ahora una función que agrega 10
print(add_10(5))  # Imprime 15 porque 10 + 5 =