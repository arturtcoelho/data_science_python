import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Datos
np.random.seed(42)
df = pd.DataFrame({
    "x": np.random.randn(100),
    "y": np.random.randn(100),
    "categoria": np.random.choice(["A", "B", "C"], 100),
    "valor": np.random.randint(10, 100, 100)
})

# Scatter interactivo
fig = px.scatter(df, x="x", y="y", color="categoria", 
                 title="Scatter interactivo",
                 hover_data=["valor"])
fig.show()

# Line chart
df_line = pd.DataFrame({
    "mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
    "ventas": [1200, 1900, 1500, 2200, 2100, 2600],
    "gastos": [800, 1000, 900, 1200, 1100, 1400]
})
fig = px.line(df_line, x="mes", y=["ventas", "gastos"],
              title="Ventas y Gastos")
fig.show()

# Bar chart
fig = px.bar(df_line, x="mes", y="ventas", 
             color="ventas", title="Ventas por mes")
fig.show()

# Box plot
fig = px.box(df, x="categoria", y="valor", 
             title="Distribución por categoría")
fig.show()

# Histogram
fig = px.histogram(df, x="valor", nbins=20, 
                   title="Histograma interactivo")
fig.show()

# Gráfico 3D
fig = px.scatter_3d(df, x="x", y="y", z="valor",
                    color="categoria", title="3D Scatter")
fig.show()

# Multiple subplots con go
fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 2, 3], name="Línea 1"))
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[3, 2, 1], name="Línea 2"))
fig.update_layout(title="Subplots con go", 
                  xaxis_title="X", yaxis_title="Y")
fig.show()
