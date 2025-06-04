import threading

def imprimir():
    for i in range(3):
        print("Hola desde un hilo")

thread = threading.Thread(target=imprimir)
thread.start()
print("Hola desde el proceso principal")