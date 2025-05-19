import time
import matplotlib.pyplot as plt

# Tamaños de n para probar
ns = [10, 100, 300, 500, 700, 900]

# Guardar los tiempos
times_single = []
times_double = []

# ---- 1 BUCLE (O(n)) ----
for n in ns:
    start = time.time()
    for i in range(n):
        x = i * 2  # operación simple
    end = time.time()
    times_single.append(end - start)

# ---- 2 BUCLES (O(n²)) ----
for n in ns:
    start = time.time()
    for i in range(n):
        for j in range(n):
            x = i * j  # operación simple
    end = time.time()
    times_double.append(end - start)

# ---- GRAFICAR ----
plt.plot(ns, times_single, marker='o', label='1 bucle (O(n))')
plt.plot(ns, times_double, marker='s', label='2 bucles (O(n²))')

plt.title('Comparación de complejidad: O(n) vs O(n²)')
plt.xlabel('n (tamaño del input)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.legend()
plt.grid(True)
plt.show()
