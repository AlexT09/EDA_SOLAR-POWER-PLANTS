# 7. Conclusiones del EDA

## Hallazgos

1. **Desbalance severo:** 75 % Alta, 22 % Media y 3 % Baja. La exactitud engaña; hay que evaluar con **F1 macro y recall por clase**.
2. **La ubicación domina:** `longitude` es, con diferencia, la variable que más separa las clases (ε² = 0.22; ninguna otra pasa de 0.05). Alta está en Asia oriental, Baja en Europa y Media en Europa y EE. UU. Funciona más como indicador de región que como causa física.
3. **Logística y altura aportan una señal débil:** las plantas Baja están más lejos de las vías (`dist_to_road`) y a mayor altura (`elevation`).
4. **Las variables climáticas son débiles por sí solas:** `ghi`, `humidity`, `ambient_temperature` y `wind_direction` casi no separan las clases (ε² < 0.015). Conviene usar modelos que capten interacciones (árboles y ensambles).
5. **Redundancia:** `latitude`, `optimal_tilt` y `ambient_temperature` forman un bloque muy correlacionado (ρ entre 0.82 y 0.91 en valor absoluto): las tres miden la distancia al ecuador.
6. **Calidad:** las 10 predictoras no tienen nulos; hay 6 406 filas duplicadas en predictoras y clase, una cola extrema en `dist_to_road` y unos pocos ceros imposibles en `ghi`, `humidity` y `wind_speed`.

## Decisiones de preprocesamiento

Todo se ajusta solo con el conjunto de entrenamiento.

- **Variables:** usar las 10 predictoras de la segunda entrega. Excluir `slope`, `aspect`, `curvature` y sus versiones categóricas por fuga de datos, además de `solar_aptitude`, `solar_aptitude_rounded`, `capacity` y `pv_potential`.
- **Duplicados:** eliminarlos antes de partir los datos.
- **Partición:** 80/20 estratificada y validación cruzada estratificada de 5 pliegues.
- **Ceros imposibles:** pasarlos a nulos e imputarlos con la mediana.
- **Extremos:** logaritmo en `dist_to_road` y recorte en el percentil 99 para KNN y SVM.
- **Codificación:** seno y coseno para `wind_direction`.
- **Colinealidad:** en la regresión logística, probar sin `optimal_tilt` o con regularización.
- **Escalado:** `StandardScaler` para los modelos sensibles a la escala.
- **Desbalance:** comparar `class_weight='balanced'`, SMOTE y ADASYN dentro de los pliegues.
- **Robustez:** vigilar que el modelo no se limite a memorizar la región a través de `longitude`; evaluar también con validación agrupada por país.
