import pandas as pd
import numpy as np

df = pd.read_csv("empleados.csv")

# print("Original:")
# print(df)
# print(f"\nValores nulos:\n{df.isnull().sum()}")

# print()

# # Detectar nulos
# print(df.isnull())
# print()
# print(df.notnull())

# Eliminar filas/columnas con nulos
# df_sin_nulos = df.dropna()
# print()
# print(df_sin_nulos)

df = df.replace(0, np.nan)

# Llenar nulos
df_llenado = df.fillna({
    "nombre": "Desconocido",
    "edad": df["edad"].mean(),
    "salario": df["salario"].median(),
    "ciudad": "Sin ciudad"
})
print("\nCon fillna:")
print(df_llenado)

# # Eliminar duplicados
# df_con_dup = pd.DataFrame({
#     "nombre": ["Ana", "Carlos", "Ana", "Marta"],
#     "edad": [28, 35, 32, 42]
# })
# print("\nSin duplicados:")
# print(df_con_dup.drop_duplicates())

# Transformar tipos
df["edad"] = df["edad"].astype("Int64")  # nullable int
print(f"\nTipo de edad: {df['edad'].dtype}")
