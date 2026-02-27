"""Ejercicio 3 – Mini flujo de regresión para predecir popularidad."""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import ExtraTreesRegressor

df = pd.read_csv("dataset.csv", index_col=0)
features = [
    "danceability",
    "energy",
    "loudness",
    "tempo",
    "valence",
    "duration_ms",
    "acousticness",
]
data = df[features + ["popularity"]].dropna()
X = data[features]
y = data["popularity"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    "LinearRegression": LinearRegression(),
    "Tree": DecisionTreeRegressor(max_depth=6),
    "ExTrees": ExtraTreesRegressor(max_depth=6, n_estimators=100)
}

metrics = {}
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    preds = model.predict(X_test_scaled)

    metrics[name] = {
        "rmse": root_mean_squared_error(y_test, preds),
        "r2": r2_score(y_test, preds),
    }

print("Métricas (RMSE, R²) sobre el conjunto de prueba:")
for name, vals in metrics.items():
    print(f" - {name}: RMSE={vals['rmse']:.2f}, R²={vals['r2']:.2f}")

coef_df = pd.DataFrame(
    {"feature": features, "linear_coef": models["LinearRegression"].coef_}
).sort_values("linear_coef", key=abs, ascending=False)

print("\nCoeficientes del modelo lineal ordenados por magnitud:")
print(coef_df.to_string(index=False, float_format="{:.3f}".format))
