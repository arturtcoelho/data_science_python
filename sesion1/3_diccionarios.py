# Diccionarios en Python

# Crear un diccionario
persona = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Madrid",
    "Skills": ["Python", "SQL", "Excel"]
}

# Acceder a valores
print(persona["nombre"])
print(persona.get("email", "No encontrado"))  # con valor por defecto

# Métodos principales
print(persona.keys())    # todas las claves
print(persona.values())  # todos los valores
print(persona.items())   # pares clave-valor

# Modificar diccionario
persona["edad"] = 31              # actualizar
persona["email"] = "carlos@ejemplo.com"  # añadir
persona.update({"pais": "España", "edad": 32})  # actualizar varios

# Eliminar
del persona["ciudad"]
email = persona.pop("email")

# Iterar
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Dict comprehension
cuadrados_dict = {x: x**2 for x in range(5)}
print(cuadrados_dict)
