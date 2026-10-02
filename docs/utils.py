"""Funciones compartidas del EDA de aptitud solar fotovoltaica.

Centraliza la carga de datos, la definición de roles de las variables, el
estilo de los gráficos y las pruebas estadísticas usadas en varios capítulos.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

SEED = 42
DATA_PATH = Path(__file__).resolve().parent / "data" / "Dataset_Mundial_Final.csv"

TARGET = "solar_aptittude_class"
CLASS_ORDER = ["Baja", "Media", "Alta"]

# Las 10 predictoras de la segunda entrega (todas numéricas).
NUMERIC = [
    "latitude", "longitude", "elevation", "dist_to_road", "ambient_temperature",
    "ghi", "humidity", "wind_speed", "wind_direction", "optimal_tilt",
]
# slope, aspect y curvature entran en la fórmula del índice de aptitud;
# sus versiones categóricas (*_type) son la misma información discretizada.
EXCLUDED_LEAKAGE = [
    "slope", "aspect", "curvature", "slope_type", "aspect_type",
    "curvature_type", "solar_aptitude", "solar_aptitude_rounded",
]
EXCLUDED_OTHER = ["capacity", "pv_potential"]
NOT_USED = ["area", "size", "dt_wind", "operational_status"]
IDENTIFIERS = ["OBJECTID", "code", "plant_name"]
DESCRIPTIVE = ["country"]

# Rótulo con unidades de cada predictora, para los ejes de los gráficos.
AXIS_LABELS = {
    "latitude": "Latitud (°)",
    "longitude": "Longitud (°)",
    "elevation": "Elevación (m s. n. m.)",
    "dist_to_road": "Distancia a la vía (m)",
    "ambient_temperature": "Temperatura media anual (°C)",
    "ghi": "Irradiación global (kWh/m²/día)",
    "humidity": "Humedad relativa (%)",
    "wind_speed": "Velocidad del viento (m/s)",
    "wind_direction": "Dirección del viento (°)",
    "optimal_tilt": "Inclinación óptima (°)",
}

# Colores fijos por clase (paleta categórica validada para daltonismo):
# el color sigue a la clase en todos los capítulos.
CLASS_COLORS = {"Alta": "#2a78d6", "Baja": "#eb6834", "Media": "#1baf7a"}
NEUTRAL = "#52514e"
SURFACE = "#fcfcfb"


def load_data(path=DATA_PATH):
    """Carga el dataset mundial de plantas solares.

    Parameters
    ----------
    path : str or Path
        Ruta al CSV separado por ``;`` con coma decimal.

    Returns
    -------
    pandas.DataFrame
        58 978 filas y 29 columnas, con la clase objetivo como categórica
        ordenada ``Baja < Media < Alta``.
    """
    df = pd.read_csv(path, sep=";", decimal=",", encoding="utf-8-sig")
    df[TARGET] = pd.Categorical(df[TARGET], categories=CLASS_ORDER, ordered=True)
    return df


def variable_roles():
    """Tabla con el rol de cada columna en el modelado.

    Returns
    -------
    pandas.DataFrame
        Columnas ``variable`` y ``rol``.
    """
    rows = (
        [(v, "Objetivo") for v in [TARGET]]
        + [(v, "Predictora") for v in NUMERIC]
        + [(v, "Excluida por fuga de datos") for v in EXCLUDED_LEAKAGE]
        + [(v, "Excluida") for v in EXCLUDED_OTHER]
        + [(v, "Excluida") for v in NOT_USED]
        + [(v, "Identificador") for v in IDENTIFIERS]
        + [(v, "Descriptiva (no predictora)") for v in DESCRIPTIVE]
    )
    return pd.DataFrame(rows, columns=["variable", "rol"])


def set_style():
    """Aplica un estilo sobrio y consistente a todos los gráficos."""
    plt.rcParams.update({
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "axes.edgecolor": "#c3c2b7",
        "axes.labelcolor": "#0b0b0b",
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.labelsize": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "axes.axisbelow": True,
        "grid.color": "#e6e5e0",
        "grid.linewidth": 0.6,
        "xtick.color": NEUTRAL,
        "ytick.color": NEUTRAL,
        "font.size": 10,
        "legend.frameon": False,
        "figure.dpi": 110,
    })


def kruskal_by_class(df, col, target=TARGET):
    """Prueba de Kruskal-Wallis de una variable numérica entre clases.

    Parameters
    ----------
    df : pandas.DataFrame
    col : str
        Variable numérica.
    target : str
        Variable de clase.

    Returns
    -------
    dict
        Estadístico H, p-valor y tamaño del efecto épsilon² (0.01 pequeño,
        0.06 mediano, 0.14 grande).
    """
    groups = [df.loc[df[target] == k, col].dropna() for k in CLASS_ORDER]
    h, p = stats.kruskal(*groups)
    n = sum(len(g) for g in groups)
    return {"H": h, "p_valor": p, "epsilon2": h / ((n ** 2 - 1) / (n + 1))}
