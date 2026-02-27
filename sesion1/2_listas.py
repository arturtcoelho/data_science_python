# Listas en Python

# Crear una lista
frutas = ["manzana", "banana", "cereza"]
numeros = [1, 2, 3, 4, 5]
mixta = [1, "hola", 3.14, True]

# Indexación (0-based)
print(frutas[0])   # primera
print(frutas[-1])  # última

# Slicing
print(numeros[1:4])   # elementos 1, 2, 3
print(numeros[:3])    # hasta el índice 3
print(numeros[::2])   # cada 2 elementos

# Métodos principales
frutas.append("naranja")      # añadir al final
frutas.insert(1, "uva")       # insertar en posición
frutas.remove("banana")        # eliminar por valor
frutas.pop()                   # eliminar último
frutas.sort()                  # ordenar
frutas.reverse()               # inverter

# List comprehension
cuadrados = [x**2 for x in range(10)]
pares = [x for x in range(20) if x % 2 == 0]

print(f"Cuadrados: {cuadrados}")
print(f"Pares: {pares}")

# Tuplas (inmutables)
coordenadas = (10, 20)
x, y = coordenadas
print(f"X: {x}, Y: {y}")

# Sets (sin duplicados)
numeros_set = {1, 2, 3, 2, 1}
print(numeros_set)  # {1, 2, 3}
