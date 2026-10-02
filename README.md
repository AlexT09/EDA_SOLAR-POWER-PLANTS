# EDA · Aptitud solar fotovoltaica

Análisis exploratorio de datos del proyecto **Clasificación de la aptitud solar fotovoltaica a partir de variables geoespaciales y climáticas** (Programa de Ciencia de Datos, Universidad del Norte).

## Estructura

```
docs/
├── _config.yml, _toc.yml       # configuración del Jupyter Book
├── intro.md                    # presentación del problema
├── 01_carga_estructura.ipynb   # dimensiones y tipos variables
├── 02_calidad_datos.ipynb      # nulos, duplicados y outliers
├── 04_univariado.ipynb         # variable objetivo y distribuciones de las 10 predictoras
├── 05_geografico.ipynb         # mapa y composición por país
├── 06_bivariado.ipynb          # predictoras frente a la clase y correlación entre ellas
├── 07_conclusiones.md          # hallazgos para preprocesamiento
├── utils.py                    # funciones compartidas
└── data/Dataset_Mundial_Final.csv
```

## Actualizar el repo y el libro

Después de editar y guardar los archivos, desde la raíz del repo:

```bash
# 1. Subir los cambios a main
git add .
git commit -m "Describe el cambio"
git push origin main

# 2. Reconstruir el libro desde cero (ejecuta todos los notebooks)
jupyter-book clean docs --all
jupyter-book build docs

# 3. Publicar en GitHub Pages (rama gh-pages)
ghp-import -n -p -f docs/_build/html
```

El sitio se actualiza en 1–2 minutos: https://alext09.github.io/EDA_SOLAR-POWER-PLANTS/intro.html
