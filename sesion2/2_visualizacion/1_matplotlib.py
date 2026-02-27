import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Figura y axes
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Seno")
ax.set_xlabel("X")
ax.set_ylabel("Y")
# plt.show()
plt.savefig("grafico1.png", dpi=300)

# Múltiples subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Gráfico de líneas
axes[0, 0].plot([1, 2, 3], [1, 4, 9], label="cuadrados", color="blue")
axes[0, 0].plot([1, 2, 3], [1, 2, 3], label="lineal", color="red")
axes[0, 0].legend()
axes[0, 0].set_title("Líneas")

# Gráfico de barras
ejes = ["A", "B", "C", "D"]
valores = [3, 7, 2, 5]
axes[0, 1].bar(ejes, valores, color=["red", "green", "blue", "orange"])
axes[0, 1].set_title("Barras")

# Histograma
datos = np.random.normal(100, 15, 1000)
axes[1, 0].hist(datos, bins=30, edgecolor="black")
axes[1, 0].set_title("Histograma")

# Scatter
x_scatter = np.random.randn(50)
y_scatter = np.random.randn(50)
axes[1, 1].scatter(x_scatter, y_scatter, alpha=0.5, c="purple")
axes[1, 1].set_title("Scatter")

plt.tight_layout()
plt.savefig("grafico2.png", dpi=300)
