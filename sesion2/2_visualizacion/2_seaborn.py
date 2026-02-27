import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Datos de ejemplo
np.random.seed(42)
df = pd.DataFrame({
    "edad": np.random.randint(20, 60, 100),
    "salario": np.random.randint(1500, 5000, 100),
    "departamento": np.random.choice(["IT", "Ventas", "RRHH", "Marketing"], 100),
    "satisfaction": np.random.randint(1, 10, 100)
})

# Estilo
sns.set_style("whitegrid")

# Distribution plot
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.histplot(df["salario"], kde=True, ax=axes[0])
axes[0].set_title("Distribución de salarios")

# Boxplot
sns.boxplot(x="departamento", y="salario", data=df, ax=axes[1])
axes[1].set_title("Salario por departamento")
plt.tight_layout()
plt.show()

# Scatter plot con regresión
plt.figure(figsize=(8, 6))
sns.regplot(x="edad", y="salario", data=df)
plt.title("Edad vs Salario")
plt.show()

# Heatmap de correlación
plt.figure(figsize=(8, 6))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
plt.title("Correlación")
plt.show()

# Countplot (barras para categorías)
plt.figure(figsize=(8, 5))
sns.countplot(x="departamento", data=df, palette="Set2")
plt.title("Empleados por departamento")
plt.show()

# Violin plot
plt.figure(figsize=(8, 5))
sns.violinplot(x="departamento", y="satisfaction", data=df)
plt.title("Satisfacción por departamento")
plt.show()

# Pairplot (todas las variables)
# sns.pairplot(df, hue="departamento")
# plt.show()
