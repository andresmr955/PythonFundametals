def my_string(x: str):
    if not isinstance(x, str):
        raise TypeError("We were waiting a string")
    print(x)

my_string(4)