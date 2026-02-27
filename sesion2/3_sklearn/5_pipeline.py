from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

# Datos mixtos (numéricos y categóricos)
np.random.seed(42)
df = pd.DataFrame({
    "edad": np.random.randint(20, 60, 200),
    "salario": np.random.randint(1500, 5000, 200),
    "ciudad": np.random.choice(["Madrid", "Barcelona", "Sevilla"], 200),
    "genero": np.random.choice(["M", "F"], 200),
    "comprado": np.random.choice([0, 1], 200, p=[0.6, 0.4])
})

# Separar features y target
X = df.drop("comprado", axis=1)
y = df["comprado"]

# Definir tipos de columnas
numericas = ["edad", "salario"]
categoricas = ["ciudad", "genero"]

# Preprocesadores
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numericas),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categoricas)
    ]
)

# Pipeline completo
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
])

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar
pipeline.fit(X_train, y_train)

# Predecir
y_pred = pipeline.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")

# GridSearch dentro del pipeline
from sklearn.model_selection import GridSearchCV

param_grid = {
    "classifier__n_estimators": [50, 100],
    "classifier__max_depth": [5, 10, None]
}

grid = GridSearchCV(pipeline, param_grid, cv=3, scoring="accuracy")
grid.fit(X_train, y_train)
print(f"\nMejor score: {grid.best_score_:.4f}")
print(f"Mejores params: {grid.best_params_}")

# Predicción con el mejor modelo
print(f"Accuracy final: {accuracy_score(y_test, grid.predict(X_test)):.4f}")
