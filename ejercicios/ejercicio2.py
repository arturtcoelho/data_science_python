"""Ejercicio 2 – Exploración con pandas y visualización."""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("dataset.csv", index_col=0)

# Estadísticos descriptivos
stats = df[["popularity", "danceability", "energy"]].describe().round(2)
print("Estadísticos descriptivos:")
print(stats)

# Top 5 canciones por popularidad
top5 = (
    df.nlargest(5, "popularity")[
        ["track_name", "artists", "track_genre", "popularity"]
    ]
    .reset_index(drop=True)
)
print("\nTop 5 de canciones por popularidad:")
print(top5.to_string(index=False))

# Promedio de popularidad por género
genre_popularity = df.groupby("track_genre")["popularity"].mean().round(2)
best_genre = genre_popularity.idxmax()
print(
    f"Género con mayor popularidad promedio: {best_genre} ({genre_popularity[best_genre]:.2f})"
)

# Top generos por danceability y sus energy
genre_table = (
    df.groupby("track_genre")[["danceability", "energy"]]
    .mean()
    .sort_values("danceability", ascending=False)
)
print("\nPromedio por género ordenado por danceability:")
print(genre_table.head(10))

### Gráfica de danceability vs energy para las 100 canciones más populares
top100 = df.nlargest(100, "popularity")
plt.figure(figsize=(9, 6))
sns.scatterplot(
    data=top100,
    x="danceability",
    y="energy",
    hue="popularity",
    palette="flare",
    size="popularity",
    sizes=(40, 200),
    alpha=0.8,
    legend=False,
)
plt.title("Danceability vs Energy en las 100 canciones más populares")
plt.xlabel("Danceability")
plt.ylabel("Energy")
plt.grid(True, linestyle="--", alpha=0.4)
plt.savefig("top100_dance_energy.png")
# plt.show()
plt.close()
print("Gráfica guardada en top100_dance_energy.png")
