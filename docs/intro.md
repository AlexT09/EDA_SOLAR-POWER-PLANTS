# Análisis exploratorio de datos: aptitud solar fotovoltaica

**Clasificación de la aptitud solar fotovoltaica a partir de variables geoespaciales y climáticas**

*Jesús David Arévalo Montilla · Enmanuel David Díaz Molinares · Alex David Terán Meza*
Programa de Ciencia de Datos, Universidad del Norte, Barranquilla.

## Problema

Antes de invertir en una planta solar hay que saber si el sitio es apto. Este proyecto busca predecir la **clase de aptitud solar** de un sitio (`solar_aptittude_class`: **Baja, Media o Alta**) a partir de sus características de terreno, clima y ubicación. Es un problema de **clasificación multiclase desbalanceada**.

## Datos

- **Archivo:** `Dataset_Mundial_Final.csv`.
- **Contenido:** 58 978 plantas fotovoltaicas de 183 países, descritas por 29 columnas.
- **Predictoras:** 17 (13 numéricas y 4 categóricas). Son las mismas usadas en la segunda entrega, donde una regresión logística multinomial fijó la línea base: F1 macro de 0.62–0.65 y ROC AUC macro de 0.886.

## Objetivo de este EDA

1. Describir la estructura y la calidad del dataset.
2. Caracterizar el desbalance de la variable objetivo.
3. Identificar qué predictoras separan mejor las clases y cómo se relacionan entre sí.
4. Justificar las variables excluidas por fuga de datos.
5. Traducir los hallazgos en **decisiones concretas de preprocesamiento** para los modelos de las siguientes etapas.

## Contenido

```{tableofcontents}
```

## Reproducibilidad

Todos los capítulos se ejecutan al compilar el libro. Usan una semilla global `SEED = 42` y las funciones compartidas de `utils.py`. Para compilarlo localmente:

```bash
pip install -r requirements.txt
jupyter-book build docs
```
