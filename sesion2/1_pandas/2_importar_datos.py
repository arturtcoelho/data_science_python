import pandas as pd
import numpy as np

# Crear DataFrame de ejemplo
df = pd.DataFrame({
    "nombre": ["Ana", "Carlos", "Marta", "Luis"],
    "edad": [28, 35, 42, 31],
    "salario": [2500, 3200, 4500, 2800],
    "departamento": ["Ventas", "IT", "Marketing", "IT"]
})

# Guardar como CSV
df.to_csv("empleados.csv", index=False)

# Leer CSV
df_csv = pd.read_csv("empleados.csv")
print("Desde CSV:")
print(df_csv)

# Leer Excel
# df.to_excel("empleados.xlsx", index=False)
# df_xlsx = pd.read_excel("empleados.xlsx")

# Leer JSON
df.to_json("empleados.json", orient="records", indent=2)
df_json = pd.read_json("empleados.json")
print("\nDesde JSON:")
print(df_json)

# Opciones de lectura
# skiprows=n: omitir primeras n filas
# nrows=n: leer solo primeras n filas
# usecols=['col1', 'col2']: seleccionar columnas

# Limpiar
import os
for f in ["empleados.csv", "empleados.json"]:
    if os.path.exists(f):
        os.remove(f)
