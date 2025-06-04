def local_function():
    x = 10
    print(x)

local_function()    

##print(x) Dont print cause is local

x = 100

def show_global():
    print(f'The value of a global variable is {x}')
show_global()    