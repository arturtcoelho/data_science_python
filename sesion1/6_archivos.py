# Archivos y Entrada/Salida en Python

# Leer archivo de texto
# Modo 'r' = lectura
with open("datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)

# Leer línea por línea
with open("datos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())

# Escribir archivo (sobrescribe)
with open("salida.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Primera línea\n")
    archivo.write("Segunda línea\n")

# Añadir contenido (append)
with open("salida.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Tercera línea\n")

# Leer y escribir CSV
import csv

# Escribir CSV
with open("datos.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre", "edad", "ciudad"])
    escritor.writerow(["Ana", 28, "Madrid"])
    escritor.writerow(["Carlos", 35, "Barcelona"])

# Leer CSV
with open("datos.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)

# JSON
import json

# Escribir JSON
datos = {"nombre": "Ana", "edad": 28, "skills": ["Python", "SQL"]}
with open("datos.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=2)

# Leer JSON
with open("datos.json", "r", encoding="utf-8") as archivo:
    datos_leidos = json.load(archivo)
    print(datos_leidos)

# pathlib (moderno)
from pathlib import Path

ruta = Path("carpeta/archivo.txt")
print(ruta.name)       # archivo.txt
print(ruta.stem)       # archivo
print(ruta.suffix)     # .txt
print(ruta.parent)     # carpeta

# Crear directorio
Path("nueva_carpeta").mkdir(exist_ok=True)
