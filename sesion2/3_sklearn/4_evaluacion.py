from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, roc_auc_score, roc_curve, 
                             mean_squared_error, r2_score)
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import numpy as np
import matplotlib.pyplot as plt

# Datos
X, y = make_classification(n_samples=200, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo
modelo = LogisticRegression(random_state=42)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
y_proba = modelo.predict_proba(X_test)[:, 1]

# Métricas de clasificación
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_proba))

# Curva ROC
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f"ROC (AUC = {roc_auc_score(y_test, y_proba):.3f})")
plt.plot([0, 1], [0, 1], "k--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Curva ROC")
plt.legend()
plt.show()

# Cross-validation
cv_scores = cross_val_score(modelo, X, y, cv=5, scoring="accuracy")
print(f"\nCV Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std()*2:.4f})")

# GridSearchCV
param_grid = {
    "C": [0.1, 1, 10],
    "max_iter": [100, 200]
}
grid_search = GridSearchCV(LogisticRegression(random_state=42), 
                           param_grid, cv=5, scoring="accuracy")
grid_search.fit(X_train, y_train)
print(f"\nMejores parámetros: {grid_search.best_params_}")
print(f"Mejor CV score: {grid_search.best_score_:.4f}")

# Métricas de regresión
from sklearn.linear_model import LinearRegression
X_reg, y_reg = make_classification(n_samples=200, n_features=1, noise=10, random_state=42)
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_reg, y_reg, test_size=0.2)

reg = LinearRegression()
reg.fit(X_train_r, y_train_r)
y_pred_r = reg.predict(X_test_r)

print("\n--- Métricas Regresión ---")
print("R2:", r2_score(y_test_r, y_pred_r))
print("RMSE:", np.sqrt(mean_squared_error(y_test_r, y_pred_r)))
print("MAE:", np.mean(np.abs(y_test_r - y_pred_r)))
