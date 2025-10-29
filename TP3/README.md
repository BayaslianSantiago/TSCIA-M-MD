# Reporte de Proyecto: Análisis y Predicción de Precios de Viviendas en California

### 1. Objetivo del proyecto
El objetivo de este proyecto es analizar las características de los vecindarios en California y predecir el precio medio de las viviendas utilizando un modelo de regresión lineal.
Se busca identificar qué factores influyen más en los precios y generar un modelo que pueda estimar el valor de una vivienda a partir de variables socioeconómicas y geográficas.

---

### 2. Descripción del dataset
Se utilizó el California Housing Dataset que contiene información de diferentes distritos de California.
Las columnas principales y son:

| Variable          | Significado                                                   |
| ----------------- | ------------------------------------------------------------- |
| Longitud          | Coordenada geográfica (grados oeste)                          |
| Latitud           | Coordenada geográfica (grados norte)                          |
| EdadCasa          | Edad media de las viviendas (años)                            |
| TotalHabitaciones | Número total de habitaciones en el distrito                   |
| TotalDormitorios  | Número total de dormitorios en el distrito                    |
| Poblacion         | Población total del distrito                                  |
| Hogares           | Número total de hogares                                       |
| IngresoMedio      | Ingreso medio del vecindario (en decenas de miles de dólares) |
| PrecioMedio       | Precio medio de las viviendas (dólares)                       |

Se añadieron columnas derivadas para facilitar el análisis:

| Variable derivada        | Fórmula                              | Significado                                                 |
| ------------------------ | ------------------------------------ | ----------------------------------------------------------- |
| HabitacionesPorHogar     | TotalHabitaciones / Hogares          | Promedio de habitaciones por hogar                          |
| DormitoriosPorHabitacion | TotalDormitorios / TotalHabitaciones | Proporción de dormitorios respecto al total de habitaciones |
| PersonasPorHogar         | Poblacion / Hogares                  | Número promedio de personas por hogar                       |

---

### 3. Análisis exploratorio de datos
Se realizaron análisis estadísticos y visualizaciones, incluyendo:
1. Mapa de calor de correlaciones:
  * Permitió identificar qué variables tienen mayor relación con el precio medio (PrecioMedio).
  * Variables con alta correlación positiva: IngresoMedio y HabitacionesPorHogar.
  * Variables con correlación negativa: Latitud y PersonasPorHogar.
2. Interpretación de correlaciones:
  * El ingreso medio del vecindario es el factor más importante para predecir el precio.
  * La distribución de habitaciones y el tamaño promedio de los hogares también influyen.
  * La ubicación geográfica (latitud) muestra un efecto negativo: distritos más al norte tienden a tener precios menores.

---

### 4. Modelo de predicción

Se entrenó un modelo de regresión lineal utilizando las variables más relevantes:
* Variables predictoras: IngresoMedio, EdadCasa, HabitacionesPorHogar, DormitoriosPorHabitacion, PersonasPorHogar, Latitud, Longitud.
* Variable objetivo: PrecioMedio.

#### Métricas de evaluación del modelo

| Métrica                                | Valor  | Interpretación                                                              |
| -------------------------------------- | ------ | --------------------------------------------------------------------------- |
| MAE (Error absoluto medio)             | ~7 500 | En promedio, el modelo se equivoca en $7 500 por casa                       |
| RMSE (Raíz del error cuadrático medio) | ~9 000 | Penaliza más los errores grandes, representa la desviación típica del error |
| R² (Coeficiente de determinación)      | ~0.63  | El modelo explica aproximadamente el 63% de la variabilidad de los precios  |

#### Importancia de las variables según el modelo:

1. IngresoMedio → factor más influyente (positivo)
2. HabitacionesPorHogar → positivo
3. Latitud → negativo (zonas más al norte, precios más bajos)
4. PersonasPorHogar → negativo

---

### 5. Conclusiones

* El ingreso medio del vecindario es el principal determinante del precio de la vivienda en California.
* Las variables derivadas como HabitacionesPorHogar y PersonasPorHogar aportan información más clara que los totales brutos.
* El modelo de regresión lineal es útil para predecir precios con un nivel razonable de precisión, aunque no captura todas las variaciones del mercado (R² ≈ 0.63).
* Futuras mejoras podrían incluir modelos más complejos (árboles de decisión, random forest, o redes neuronales) y más variables externas (por ejemplo, cercanía a escuelas, transporte, zonas comerciales).

---

### 6. Tecnologías Implementadas

| Tecnología / Librería      | Uso en el proyecto                                                                                                                            |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Python**                 | Lenguaje principal para manipulación de datos, análisis y modelado.                                                                           |
| **Pandas**                 | Carga, limpieza y transformación del dataset; creación de nuevas columnas derivadas.                                                          |
| **NumPy**                  | Operaciones numéricas, cálculos de errores y manipulación de arreglos.                                                                        |
| **Matplotlib**             | Visualización de datos: gráficos de barras, mapas de calor y comparación de precios reales vs. predichos.                                     |
| **Scikit-learn (sklearn)** | Entrenamiento y evaluación del modelo de regresión lineal; métricas de desempeño (MAE, RMSE, R²) y división de datos en entrenamiento/prueba. |
| **Google Colab**           | Entorno de ejecución en la nube para facilitar el desarrollo, visualización y reproducibilidad del proyecto.                                  |
