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

# Pivot table
print("\nPivot table:")
print(df.pivot_table(values="salario", 
                     index="departamento", 
                     aggfunc="mean"))

# crosstab
print("\nCrosstab:")
print(pd.crosstab(df["departamento"], df["antiguedad"] > 3))

# value_counts
print("\nValue counts:")
print(df["departamento"].value_counts())
