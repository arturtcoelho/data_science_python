from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt

# Datos: relación lineal (y = 3x + ruido)
np.random.seed(42)
X = np.random.randn(100, 1) * 5
y = 3 * X + 2 + np.random.randn(100, 1) * 2

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Regresión Lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

print("Regresión Lineal")
print(f"Coeficiente (pendiente): {modelo.coef_[0][0]:.4f}")
print(f"Intercepto: {modelo.intercept_[0]:.4f}")
print(f"R2 Score: {r2_score(y_test, y_pred):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")

# Visualización
plt.scatter(X_test, y_test, color="blue", label="Real")
plt.plot(X_test, y_pred, color="red", label="Predicción")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.title("Regresión Lineal")
plt.show()

# Regresión Polinómica
X_poly = np.random.randn(100, 1)
y_poly = 2 * X_poly**3 + X_poly**2 + np.random.randn(100, 1) * 0.5

poly = PolynomialFeatures(degree=3)
X_poly_train = poly.fit_transform(X_poly)

modelo_poly = LinearRegression()
modelo_poly.fit(X_poly_train, y_poly)
print(f"\nR2 Polinómico: {r2_score(y_poly, modelo_poly.predict(X_poly_train)):.4f}")

# Ridge (regularización L2)
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
print(f"Ridge R2: {r2_score(y_test, ridge.predict(X_test)):.4f}")

# Lasso (regularización L1)
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)
print(f"Lasso R2: {r2_score(y_test, lasso.predict(X_test)):.4f}")
