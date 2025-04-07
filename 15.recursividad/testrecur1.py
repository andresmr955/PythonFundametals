def fibonacci(n):
    print(f"Entering fibonacci({n})")  # Imprime cuando entras en una llamada recursiva
    if n <= 1:
        return n
    else:
       
        result = fibonacci(n - 1) + fibonacci(n - 2)  # Recursión
        print(f"Returning fibonacci({n}) = {result}")  # Imprime cuando sales de una llamada recursiva
        return result

# Llamada principal
print(fibonacci(5))  # Puedes cambiar el número aquí para ver diferentes resultados

