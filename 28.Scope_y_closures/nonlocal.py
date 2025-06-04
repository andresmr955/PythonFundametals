def outer_function():
    x = 'enclosing'
    print(f'This is first x {id(x)}')
    def inner_function():
        nonlocal x 
        x = 'modified'
        print(f'El valor en inner es: {id(x)}')
    inner_function()
    print(f'El valor outer: {id(x)}')
outer_function()