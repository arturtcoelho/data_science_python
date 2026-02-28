# Control de flujo en Python

print(1)

# Condicionales
edad = 18

if edad < 18:
    print("Menor de edad")
elif edad < 65:
    print("Adulto")
else:
    print("Jubilado")

# Operadores lógicos
nota = 85
if nota >= 90 and nota <= 100:
    print("Sobresaliente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Suspenso")

# Bucle for
frutas = ["manzana", "banana", "cereza"]

for letra in "manzana":
    print(f"letra: {letra}")

# range()
l = []
for i in range(1, 100):
    l.append(i)
print(l)

print([i for i in range(100)])

for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# enumerate
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")


# Control: break y continue
for n in range(10):
    if n == 3:
        continue  # salta a la siguiente iteración
    if n == 7:
        break     # sale del bucle
    print(n)

# Comprehensions (resumen de bucles)
lista = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in lista]
pares = [x for x in lista if x % 2 == 0]
