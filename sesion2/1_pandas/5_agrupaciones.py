import pandas as pd
import numpy as np

df = pd.DataFrame({
    "departamento": ["Ventas", "IT", "Marketing", "Ventas", "IT", "Marketing"],
    "empleado": ["Ana", "Carlos", "Marta", "Luis", "Elena", "Pedro"],
    "salario": [2500, 3200, 4500, 2800, 3100, 4200],
    "antiguedad": [2, 5, 8, 1, 4, 7]
})

# groupby - agrupar por columna
print("Groupby departamento:")
print(df.groupby("departamento").size())

# Agregaciones
print("\nMedia por departamento:")
print(df.groupby("departamento")["salario"].mean())

print("\nMúltiples agregaciones:")
print(df.groupby("departamento").agg({
    "salario": ["mean", "sum", "max"],
    "antiguedad": "mean"
}))

# transform (mantiene forma original)
df["salario_media_dept"] = df.groupby("departamento")["salario"].transform("mean")
print("\nCon media por dept:")
print(df)


# Ejemplo de pivote con meses
ventas = pd.DataFrame({
    "cliente": ["Uvas", "Manzanas", "Platanos"],
    "producto": ["España", "Portugal", "Francia"],
    "ene": [1, 2, 3],
    "feb": [4, 5, 6],
    "mar": [7, 8, 9]
})

print("\nVentas por meses (wide):")
print(ventas)

ventas_long = ventas.melt(id_vars=["cliente", "producto"], 
                          var_name="mes", 
                          value_name="valor")

print("\nVentas pivotadas (long):")
print(ventas_long)
