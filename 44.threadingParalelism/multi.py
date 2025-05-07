import multiprocessing

def calcular_cuadrado(numeros, cola):
    for n in numeros:
        cola.put(n * n)

if __name__ == "__main__":
    numeros = list(range(1, 1001))  # 100,000 números
    cola = multiprocessing.Queue()

    mitad = len(numeros) // 2
    proceso1 = multiprocessing.Process(target=calcular_cuadrado, args=(numeros[:mitad], cola))
    proceso2 = multiprocessing.Process(target=calcular_cuadrado, args=(numeros[mitad:], cola))

    proceso1.start()
    proceso2.start()

    proceso1.join()
    proceso2.join()

    resultados = []
    while not cola.empty():
        resultados.append(cola.get())

    print(f"Se calcularon {len(resultados)} cuadrados")