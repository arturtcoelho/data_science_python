import pandas as pd
import numpy as np

# DataFrame con valores nulos
df = pd.DataFrame({
    "nombre": ["Ana", "Carlos", None, "Marta", "Luis"],
    "edad": [28, 42, 35, None, 31],
    "salario": [2500, None, 3000, 4500, None],
    "ciudad": ["Madrid", "Barcelona", "Sevilla", None, "Valencia"]
})

print("Original:")
print(df)
print(f"\nValores nulos:\n{df.isnull().sum()}")

print()

# Detectar nulos
print(df.isnull())
print()
print(df.notnull())

# Eliminar filas/columnas con nulos
df_sin_nulos = df.dropna()
print()
print(df_sin_nulos)

# Llenar nulos
df_llenado = df.fillna({
    "nombre": "Desconocido",
    "edad": df["edad"].mean(),
    "salario": df["salario"].median(),
    "ciudad": "Sin ciudad"
})
print("\nCon fillna:")
print(df_llenado)

# Eliminar duplicados
df_con_dup = pd.DataFrame({
    "nombre": ["Ana", "Carlos", "Ana", "Marta"],
    "edad": [28, 35, 28, 42]
})
print("\nSin duplicados:")
print(df_con_dup.drop_duplicates())

# Transformar tipos
df["edad"] = df["edad"].astype("Int64")  # nullable int
print(f"\nTipo de edad: {df['edad'].dtype}")
