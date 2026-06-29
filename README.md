# Proyecto Integrador de Minería de Datos I

## Información general

**Carrera:** Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial.  
**Asignatura:** Minería de Datos I.  
**Profesor:** Fernando Elias Mubarqui.  
**Integrantes:** Thir Ferreyra Nadia Lorena y Constantinidi Leandro Exequiel.  
**Comisión:** Turno Tarde.  
**Título:** Análisis exploratorio de usuarios de una plataforma de streaming.  
**Fecha de cierre analítico:** 27 de junio de 2026.  
**Repositorio público:** se incorporará después de publicar en GitHub.  
**Aplicación pública:** se incorporará después del despliegue en Streamlit Cloud.

## Objetivo del proyecto

Analizar la estructura, calidad y patrones principales de un dataset de usuarios de una plataforma de streaming. El trabajo estudia la relación del plan, la edad y el país con el tiempo mensual de visualización. También aplica escalamiento y PCA para evaluar si las variables numéricas pueden resumirse. El alcance es descriptivo y no incluye modelos predictivos ni afirmaciones causales.

## Dataset

El archivo original se conserva sin modificaciones en [`data/raw/streaming_users_dirty.json`](data/raw/streaming_users_dirty.json). Cada fila representa un usuario y contiene ocho variables. La base original posee 8.160 filas; luego de resolver identificadores repetidos, la base procesada conserva 8.000 usuarios únicos. El resultado final se encuentra en [`data/processed/streaming_users_clean.csv`](data/processed/streaming_users_clean.csv). Las únicas ausencias finales corresponden a fechas que no podían interpretarse con seguridad.

## Estructura del repositorio

- [`data/`](data/): datos originales y procesados.
- [`notebooks/`](notebooks/): inspección, limpieza, EDA, PCA y conclusiones.
- [`app/`](app/): aplicación multipágina de Streamlit.
- [`reports/informe_final.pdf`](reports/informe_final.pdf): informe final breve.
- [`logs/pipeline_log.csv`](logs/pipeline_log.csv): registro de transformaciones.
- [`requirements.txt`](requirements.txt): dependencias del proyecto.

## Preparación y calidad de datos

Se conservó la primera aparición de cada `user_id` porque la inspección mostró que las últimas 160 filas repetían usuarios anteriores. Se unificaron categorías mediante diccionarios explícitos. Las edades aisladas de -5, 0, 4, 130 y 150 se trataron como inconsistentes porque no había registros entre 5 y 12 años y la distribución continua comenzaba en 13. Los minutos físicamente imposibles y los códigos inválidos de tickets se marcaron como faltantes. La edad y los tickets se imputaron con la mediana; los minutos, con la mediana de cada plan. Las fechas ambiguas, imposibles o futuras permanecieron faltantes. El detalle está en [`02_calidad_y_limpieza.ipynb`](notebooks/02_calidad_y_limpieza.ipynb) y en el [`pipeline_log.csv`](logs/pipeline_log.csv).

## Resumen del análisis exploratorio

El plan presenta la asociación descriptiva más clara con el consumo: las medianas aumentan de Básico a Estándar y Premium. La distribución de minutos es asimétrica y contiene usuarios intensivos plausibles. La relación lineal entre edad y consumo es prácticamente nula. El orden de consumo por plan se mantiene en los siete países, aunque existe superposición entre los grupos. Las cinco visualizaciones y sus interpretaciones se encuentran en [`03_eda.ipynb`](notebooks/03_eda.ipynb) y en Streamlit.

## Reducción de dimensionalidad

PCA utiliza edad, minutos mensuales, tickets y días desde el último ingreso. Antes de aplicarlo se estandarizan las variables con `StandardScaler`. Las dos primeras componentes explican aproximadamente el 50,45 % de la varianza y las tres primeras el 75,32 %. Para superar el 80 % se necesitan las cuatro componentes; por eso PCA resulta útil para explorar y visualizar, pero no permite una reducción eficiente. Véase [`04_pca.ipynb`](notebooks/04_pca.ipynb).

## Visualización interactiva

La aplicación incluye Inicio, Dataset, EDA, PCA y Conclusiones. EDA contiene exactamente dos visualizaciones univariadas, dos bivariadas y una multivariada. PCA contiene dos visualizaciones. El archivo de entrada es [`app/Home.py`](app/Home.py). El enlace público se agregará después del despliegue.

## Cómo ejecutar localmente

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app/Home.py
```

## Conclusiones

El proceso produjo un dataset reproducible de 8.000 usuarios únicos. El plan de suscripción presenta las diferencias descriptivas más claras en el consumo mensual. La edad no muestra una relación lineal relevante y el país no revierte el patrón general entre planes. PCA indica baja redundancia entre las variables seleccionadas. Los resultados describen asociaciones del dataset y no permiten establecer causalidad. La síntesis se encuentra en [`05_conclusiones.ipynb`](notebooks/05_conclusiones.ipynb).
