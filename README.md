# EDA · Aptitud solar fotovoltaica

Análisis exploratorio de datos del proyecto **Clasificación de la aptitud solar fotovoltaica a partir de variables geoespaciales y climáticas** (Programa de Ciencia de Datos, Universidad del Norte).


## Estructura

```
docs/
├── _config.yml, _toc.yml       # configuración del Jupyter Book
├── intro.md                    # presentación del problema
├── 01_carga_estructura.ipynb   # dimensiones, tipos y roles de variables
├── 02_calidad_datos.ipynb      # nulos, duplicados, extremos, categorías
├── 03_variable_objetivo.ipynb  # desbalance de solar_aptittude_class
├── 04_univariado.ipynb         # distribuciones de las 17 predictoras
├── 05_geografico.ipynb         # mapa y composición por país
├── 06_bivariado.ipynb          # Kruskal-Wallis / chi² frente a la clase
├── 07_correlacion.ipynb        # Spearman y VIF
├── 08_fuga_seleccion.ipynb     # variables excluidas y predictoras finales
├── 09_conclusiones.md          # hallazgos y decisiones de preprocesamiento
├── utils.py                    # funciones compartidas (carga, estilo, pruebas)
└── data/Dataset_Mundial_Final.csv
```
