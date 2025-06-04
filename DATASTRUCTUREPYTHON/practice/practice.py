def factorial_deNuevo(n):

    if n == 1:
        return 1
    else:
        result = n * factorial_deNuevo(n - 1)
        return result

print(factorial_deNuevo(5))