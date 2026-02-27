import pandas as pd

df = pd.DataFrame({
    "nombre": ["Ana", "Carlos", "Marta", "Luis", "Elena"],
    "edad": [28, 35, 42, 31, 29],
    "salario": [2500, 3200, 4500, 2800, 2600],
    "departamento": ["Ventas", "IT", "Marketing", "IT", "Ventas"]
})

# loc: por etiqueta
print("fila 0:", df.loc[0])
print("filas 0:2, columnas nombre y edad:")
print(df.loc[0:2, ["nombre", "edad"]])

# iloc: por posición numérica
print("\niloc[0:3, 0:2]:")
print(df.iloc[0:3, 0:2])

# Boolean indexing (filtrar con condiciones)
print("\nMayores de 30:")
print(df[df["edad"] > 30])

print("\nEn IT:")
print(df[df["departamento"] == "IT"])

# Múltiples condiciones (& | ~)
print("\nIT Y salario > 3000:")
print(df[(df["departamento"] == "IT") & (df["salario"] > 3000)])

# isin
print("\nVentas o Marketing:")
print(df[df["departamento"].isin(["Ventas", "Marketing"])])

# query
print("\nCon query:")
print(df.query("edad > 30 and salario < 4000"))

# Filtrar con str
df_nombres = pd.DataFrame({"nombre": ["Ana", "Carlos", "María"]})
print(df_nombres[df_nombres["nombre"].str.contains("a", case=False)])
