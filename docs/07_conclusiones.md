# 7. Conclusiones del EDA

## Hallazgos

1. **Desbalance severo:** 75 % Alta, 22 % Media y 3 % Baja. Hay que evaluar con **F1 macro y recall por clase**.
2. **La ubicación domina:** `longitude` es, con diferencia, la variable que más separa las clases (ε² = 0.22).
3. **Las variables climáticas son débiles por sí solas:** `ghi`, `humidity`, `ambient_temperature` y `wind_direction` casi no separan las clases (ε² < 0.015).
4. **Redundancia:** `latitude`, `optimal_tilt` y `ambient_temperature` forman un bloque correlacionado.
5. **Calidad:** las 10 predictoras no tienen nulos; hay 6 406 filas duplicadas en predictoras y clase, una cola extrema en `dist_to_road` y unos pocos ceros inconsistentes en `ghi`, `humidity` y `wind_speed`.

## Para preprocesamiento

- **Variables:** usar las 10 predictoras excluyendo `slope`, `aspect`, `curvature` y sus versiones categóricas por fuga de datos, además de `solar_aptitude`, `solar_aptitude_rounded`, `capacity` y `pv_potential`.
- **Duplicados:** eliminarlos antes de partir los datos.
- **Partición:** 80/20 estratificada y validación cruzada estratificada de 5 pliegues.
- **Ceros inconsistentes:** pasarlos a nulos e imputarlos con la mediana.
- **Extremos:** logaritmo en `dist_to_road`.
- **Codificación:** seno y coseno para `wind_direction`.
- **Colinealidad:** en la regresión logística, probar sin `optimal_tilt` o con regularización.
- **Escalado:** `StandardScaler` para los modelos sensibles a la escala.
- **Desbalance:** comparar `class_weight='balanced'`.
- **Robustez:** revisar que el modelo no se limite a memorizar la región a través de `longitude`; evaluar también con validación agrupada por país.
