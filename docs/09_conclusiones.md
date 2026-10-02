# 9. Conclusiones del EDA

## Hallazgos principales

1. **El desbalance es severo.** La distribución es 75.10 % Alta, 21.69 % Media y 3.21 % Baja (razón 23 : 1). Un clasificador trivial ya obtiene un 75 % de exactitud, por lo que la evaluación debe basarse en el **F1 macro, el recall por clase y el ROC AUC macro**.
2. **La geografía domina la señal.** `longitude` es la predictora más discriminante (ε² = 0.22). Funciona como indicador de región: Asia oriental es casi toda Alta, EE. UU. es mayoritariamente Media y la clase Baja se concentra en Europa.
3. **El terreno es la señal física.** `slope` (ε² = 0.06) y `slope_type` (V = 0.26) muestran que la pendiente pronunciada se asocia con baja aptitud. Le siguen `curvature_type`, `dist_to_road` y `elevation`: las plantas Baja están en terreno más alto, más remoto y menos plano.
4. **Hay variables débiles por sí solas.** `aspect`, `curvature` numérica, `humidity`, `ghi`, `area` y `wind_direction` casi no separan las clases de forma individual. Esto motiva modelos capaces de capturar interacciones (árboles, Random Forest, XGBoost).
5. **No hay multicolinealidad problemática.** Todos los VIF son menores de 3.5. El único par fuerte es `latitude` y `ambient_temperature` (ρ = −0.82).
6. **Hay que corregir varios problemas de calidad:**
   - Los nulos de `area` (27.69 %) **no son aleatorios**: 33 % en Alta frente a 11–12 % en Baja y Media.
   - 3 245 filas duplican a otra en predictoras y clase.
   - `area` y `dist_to_road` tienen colas extremas.
   - 3 registros tienen `ghi = 0` o `humidity = 0`.

## Decisiones de preprocesamiento

Todas se implementan dentro de un `Pipeline` / `ColumnTransformer` ajustado solo con el conjunto de entrenamiento.

| Paso | Decisión | Justificación (capítulo) |
|---|---|---|
| Variables | 17 predictoras; se excluyen `solar_aptitude`, `solar_aptitude_rounded`, `capacity`, `optimal_tilt`, `pv_potential`, `operational_status` y los identificadores | Fuga de datos o información posterior a la inversión (8) |
| Duplicados | Eliminar los 3 245 duplicados de predictoras + clase antes de la partición | Evitar que una copia esté en entrenamiento y su gemela en prueba (2) |
| Partición | 80/20 estratificada, `random_state = 42`; validación `StratifiedKFold(5)` | Preservar el 3.21 % de Baja en cada pliegue (3) |
| Nulos | Imputación por mediana en `area`, más un indicador `area_missing` | Los nulos se asocian con la clase (2) |
| Asimetría | `log1p` en `area` y `dist_to_road`; winsorización en el p99 para KNN y SVM | Asimetrías de 72.6 y 48.7 (2, 4) |
| Valores imposibles | `ghi = 0` y `humidity = 0` → nulo e imputar | Físicamente imposibles (2) |
| Variables circulares | `aspect` y `wind_direction` → seno y coseno | 0° y 360° son el mismo valor (4) |
| Categóricas | One-hot (39 columnas); agrupar niveles con menos del 1 % (`Escarpado o abrupto`, vientos N/NE/NW) | Niveles casi vacíos (4) |
| Escalado | `StandardScaler` en numéricas (KNN, SVM, logística, Ridge y Lasso) | Escalas muy distintas entre variables (4) |
| Desbalance | Comparar sin balanceo, `class_weight='balanced'`, SMOTE y ADASYN, solo dentro de los pliegues de entrenamiento | Razón de 23 : 1 (3) |
| Robustez | Validación adicional agrupada por país; revisar con SHAP el peso de las coordenadas | La clase depende de la región (5) |

## Implicaciones para la siguiente etapa

La segunda entrega dejó como referencia un **F1 macro de 0.62–0.65**. El EDA indica que el margen de mejora está en:
- **Capturar interacciones no lineales** entre terreno y clima, con árboles y ensambles.
- **Limpiar la fuga entre particiones** que generan los duplicados.
- **Aprovechar la información que hoy se descarta:** el patrón de nulos de `area` y el carácter circular de `aspect` y `wind_direction`.

Hay que vigilar especialmente que las ganancias no provengan solo de memorizar la región a través de `longitude`.
