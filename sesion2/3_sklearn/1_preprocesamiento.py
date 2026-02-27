from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np

# Datos con problemas
df = pd.DataFrame({
    "edad": [25, 30, None, 35, 28, None, 45],
    "salario": [2500, 3200, 4500, None, 2800, 3100, 4200],
    "ciudad": ["Madrid", "Barcelona", None, "Sevilla", "Madrid", "Barcelona", "Valencia"],
    "genero": ["F", "M", "F", "M", "F", "M", "F"]
})

# Imputar valores faltantes (media, mediana, más frecuente)
imputer = SimpleImputer(strategy="median")
df[["edad", "salario"]] = imputer.fit_transform(df[["edad", "salario"]])

# Imputar categóricas
df["ciudad"] = df["ciudad"].fillna("Desconocido")

print("Después de imputar:")
print(df)

# Escalado
# StandardScaler (media=0, std=1)
scaler = StandardScaler()
df[["edad", "salario"]] = scaler.fit_transform(df[["edad", "salario"]])
print("\nCon StandardScaler:")
print(df)

# MinMaxScaler (0 a 1)
minmax = MinMaxScaler()
df_mm = df.copy()
df_mm[["edad", "salario"]] = minmax.fit_transform(df_mm[["edad", "salario"]])
print("\nCon MinMaxScaler:")
print(df_mm)

# Encoding categóricas
# LabelEncoder (ordinal)
le = LabelEncoder()
df["genero_encoded"] = le.fit_transform(df["genero"])
print("\nCon LabelEncoder:")
print(df)

# OneHotEncoder (nominal)
df_onehot = pd.get_dummies(df, columns=["ciudad"], prefix="ciudad")
print("\nCon OneHotEncoder (get_dummies):")
print(df_onehot)

# Train/test split
X = df_onehot.drop("genero_encoded", axis=1)
y = df_onehot["genero_encoded"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTrain: {X_train.shape}, Test: {X_test.shape}")
