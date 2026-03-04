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

### Ejercicio 3 – Segmentación avanzada con pandas

Profundiza en EDA solo con pandas (puedes apoyarte en Matplotlib/Seaborn para gráficos simples). Trabaja en un script/notebook independiente del ejercicio 2.

1. Carga `dataset.csv`, estandariza nombres de columnas (snake_case), elimina duplicados y maneja valores nulos con reglas sencillas (relleno con medias/medianas o eliminación controlada). Resume qué hiciste.
2. Crea al menos dos columnas derivadas que ayuden a segmentar canciones (p.ej. `energy_minus_acousticness`, `tempo_range_label`). Describe brevemente el propósito de cada una.
3. Agrupa por `track_genre` y calcula: cantidad de canciones, `popularity` promedio, mediana de `danceability` y máximo de `energy`. Ordena por popularidad promedio y guarda la tabla en `reports/resumen_generos.csv`.
4. Construye una tabla “top n por género” (elige `n=3` o `5`): para cada género muestra las canciones más populares con columnas clave (`track_name`, `artist_name`, `popularity`, tus features derivadas). Exporta a `reports/top_por_genero.csv`.
5. Identifica posibles outliers de energía por género usando el rango intercuartílico (IQR). Exporta el resultado a `reports/outliers_energy.csv` con las mismas columnas del punto anterior.
6. Agrega al menos una visualización que compare géneros (ej. barras de `popularity` promedio, boxplot de `danceability`). Guarda el gráfico en `reports/` con etiquetas claras.
7. Implementa una función `genre_snapshot(df, genre)` que imprima un resumen con estadísticas clave y la lista de canciones destacadas para el género solicitado.
