import pandas as pd

# # Series (como una columna)
# s = pd.Series([1, 2, 3, 4, 5])
# print("Serie:", s.values)

# s_con_indice = pd.Series([10, 20, 30], index=["a", "b", "c"])
# print("Con índice:", s_con_indice["a"])

# DataFrame (tabla)
df = pd.DataFrame({
    "nombre": ["Ana", "Carlos", "Marta"],
    "edad": [28.5, 35, "sevilla"],
    "ciudad": ["Madrid", "Barcelona", 123],
    "bool": [True, True, False]
})
print("\nDataFrame:")
print(df)

# # Información del DataFrame
# # print(f"\nForma: {df.shape}")
# print(f"Columnas: {df.columns.tolist()}")
# print(df.dtypes)

# Acceder a columnas
print()
print(df["nombre"])
print()
print(df.edad)  # atributo

# Primeros y últimos registros
print()
print(df.head(1))
print()
print(df.tail(2))
