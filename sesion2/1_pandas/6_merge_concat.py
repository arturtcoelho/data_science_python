import pandas as pd

# DataFrames de ejemplo
df1 = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "nombre": ["Ana", "Carlos", "Marta", "Luis"],
    "departamento_id": [101, 102, 101, 103]
})

df2 = pd.DataFrame({
    "dept_id": [101, 102, 103],
    "departamento": ["Ventas", "IT", "Marketing"]
})

# merge (como SQL JOIN)
print("Merge (inner):")
print(pd.merge(df1, df2, left_on="departamento_id", right_on="dept_id"))

print("\nMerge (left):")
print(pd.merge(df1, df2, left_on="departamento_id", right_on="dept_id", how="left"))

# concat (apilar)
df3 = pd.DataFrame({
    "nombre": ["Elena", "Pedro"],
    "edad": [29, 35]
})
df4 = pd.DataFrame({
    "nombre": ["Rosa", "Jorge"],
    "edad": [41, 38]
})

print("\nConcat (vertical):")
print(pd.concat([df3, df4], ignore_index=True))

# concat horizontal
df5 = pd.DataFrame({"ciudad": ["Madrid", "Barcelona"]})
print("\nConcat (horizontal):")
print(pd.concat([df3, df5], axis=1))
