# Ejercicios por implementar

En este directorio están los datos y los retos propuestos para que practiques con los conceptos de las sesiones 1 y 2. **No hay soluciones prefabricadas**: usa este README como guía para implementar tus propios scripts o notebooks.

## Sesión 1 – Python básico

Implementa un programa que cumpla con los siguientes puntos:

1. Pide al usuario que elija una figura geométrica: rectángulo, círculo o triángulo rectángulo.
2. Solicita las dimensiones necesarias (base/altura, radio, catetos) 
3. Calcula área y perímetro (circunferencia, suma de lados con hipotenusa).

## Sesión 2 – Análisis y machine learning con pandas

El archivo `dataset.csv` contiene estadísticas de canciones (columna `track_genre`, `popularity`, `danceability`, `energy`, `loudness`, `tempo`, `acousticness`, etc.). Apóyate en el plan de la sesión 2 del README general (`../README.md`). Implementa dos scripts/notebooks independientes según los siguientes enunciados:

### Ejercicio 1 – Exploración con pandas + visualización

1. Carga el CSV en un DataFrame;
2. Imprime estadísticos descriptivos para `popularity`, `danceability` y `energy`.
3. Muestra las cinco canciones con mayor popularidad y el género con mayor popularidad promedio.
4. Agrupa por `track_genre` y lista los 10 géneros con mayor `danceability` promedio junto con su `energy` promedio.
5. Crea y guarda una gráfica (Matplotlib/Seaborn) que explore la relación entre `danceability` y `energy` para las 100 canciones más populares; usa color o tamaño para resaltar `popularity`.

### Ejercicio 2 – Mini flujo de regresión y comparación de modelos

1. Prepara un conjunto de características que incluya las caracteristicas numericas: `danceability`, `energy`, `loudness`, `valence`, `tempo`, `duration_ms` y `acousticness`.
2. Divide en entrenamiento/prueba (80/20).
3. Entrena un modelo de regrecion como `LinearRegression`. Evalúa con RMSE, `R²` sobre la prueba.
4. Entrena otro modelo distinto (por ejemplo `DecisionTreeRegressor`, `KNeighborsRegressor`). Evalúa con las mismas métricas.
5. Compara resultados: ¿cuál modelo tiene menor error?

Si quieres, guarda las predicciones del mejor modelo para inspección posterior.
