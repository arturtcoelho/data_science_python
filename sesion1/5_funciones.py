# Funciones en Python

# Función básica
def saludar():
    print("¡Hola!")

saludar()

# Con parámetros
def saludar_persona(nombre):
    print(f"¡Hola, {nombre}!")

saludar_persona("Ana")

# Con retorno
def suma(a, b):
    return a + b

resultado = suma(3, 5)
print(resultado)

# Parámetros por defecto
def potencia(base, exponente=2):
    return base ** exponente

print(potencia(3))      # 9
print(potencia(3, 3))  # 27

# Args y Kwargs
def suma_total(*args):
    return sum(args)

print(suma_total(1, 2, 3, 4, 5))

def info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

info(nombre="Ana", edad=28, ciudad="Madrid")

# Lambda (funciones anónima)
doble = lambda x: x * 2
print(doble(5))

# map y filter
numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Dobles: {dobles}")
print(f"Pares: {pares}")

# Módulos
import math
print(math.pi)
print(math.sqrt(16))

from random import randint, choice
print(randint(1, 10))
print(choice(["rojo", "verde", "azul"]))
