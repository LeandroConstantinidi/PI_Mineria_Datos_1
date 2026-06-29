# Proyecto Integrador de Minería de Datos I

## Información general

**Título:** Análisis de usuarios de una plataforma de streaming
**Carrera:** Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial
**Asignatura:** Minería de Datos I
**Comisión:** Turno Tarde
**Integrantes:**

* Thir Ferreyra Nadia Lorena
* Constantinidi Leandro Exequiel

**Fecha de elaboración:** junio de 2026

### Enlaces públicos

* [Repositorio público de GitHub](https://github.com/LeandroConstantinidi/PI_Mineria_Datos_1)
* [Aplicación pública en Streamlit](https://pi-mineria-datos-constantinidi-thir-2026.streamlit.app/)
* [Informe final en PDF](reports/informe_final.pdf)
* [Registro del proceso ETL](logs/pipeline_log.csv)

## Objetivo del proyecto

El objetivo es desarrollar un análisis reproducible y comunicable sobre usuarios de una plataforma de streaming. El trabajo comprende inspección inicial, evaluación de calidad, limpieza, preparación, análisis exploratorio y reducción de dimensionalidad mediante PCA. Las decisiones se justifican con evidencia obtenida del dataset y se registra su impacto. El alcance es descriptivo y exploratorio; no incluye modelos predictivos ni permite establecer relaciones causales.

## Dataset

El archivo original contiene 8.160 filas y 8 variables relacionadas con identificación, edad, plan de suscripción, minutos mensuales de visualización, país, género favorito, fecha del último ingreso y tickets de soporte. Se detectaron valores faltantes, duplicados, categorías escritas de distintas formas, valores numéricos incompatibles y fechas ambiguas, imposibles o futuras. El archivo original se conserva sin modificaciones en [`data/raw/streaming_users_dirty.json`](data/raw/streaming_users_dirty.json). El dataset final contiene 8.000 usuarios únicos y está disponible en [`data/processed/streaming_users_clean.csv`](data/processed/streaming_users_clean.csv).

## Estructura del repositorio

```text
PI_Mineria_Datos_1/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   │   └── streaming_users_dirty.json
│   └── processed/
│       └── streaming_users_clean.csv
├── notebooks/
│   ├── 01_inspeccion_inicial.ipynb
│   ├── 02_calidad_y_limpieza.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_pca.ipynb
│   └── 05_conclusiones.ipynb
├── app/
│   ├── Home.py
│   └── pages/
│       ├── 01_Dataset.py
│       ├── 02_EDA.py
│       ├── 03_PCA.py
│       └── 04_Conclusiones.py
├── reports/
│   └── informe_final.pdf
└── logs/
    └── pipeline_log.csv
```

## Preparación y calidad de datos

La preparación se desarrolló en [`02_calidad_y_limpieza.ipynb`](notebooks/02_calidad_y_limpieza.ipynb). Se conservaron las primeras apariciones de los identificadores luego de comprobar que las últimas filas repetían usuarios ya presentes. Los planes, países y géneros se normalizaron mediante equivalencias explícitas. Las edades incompatibles con la distribución observada, los tiempos imposibles y los códigos anómalos de tickets se transformaron en faltantes antes de imputarlos con medianas justificadas. El consumo se imputó mediante la mediana correspondiente a cada plan. Las fechas ambiguas, imposibles o futuras permanecieron como desconocidas para no inventar información. Cada transformación y su impacto se registraron en [`logs/pipeline_log.csv`](logs/pipeline_log.csv).

## Resumen del análisis exploratorio

El análisis completo se encuentra en [`03_eda.ipynb`](notebooks/03_eda.ipynb). La mayor proporción de usuarios pertenece al plan Básico, seguida por Estándar y Premium. El tiempo mensual presenta una distribución con usuarios de consumo elevado, por lo que la mediana representa mejor al usuario típico que la media. El plan de suscripción presenta la asociación descriptiva más clara con el consumo: las medianas aumentan de Básico a Estándar y Premium. La edad no muestra una relación lineal relevante con los minutos mensuales. El patrón Premium > Estándar > Básico se mantiene en los siete países, aunque los resultados describen asociaciones y no demuestran causalidad.

## Reducción de dimensionalidad

El procedimiento se documenta en [`04_pca.ipynb`](notebooks/04_pca.ipynb). PCA se aplicó a edad, minutos mensuales, tickets de soporte y días desde el último ingreso. Se utilizó `StandardScaler` porque las variables poseen unidades y rangos diferentes. Las dos primeras componentes explican el 50,45 % de la variabilidad y se necesitan las cuatro para superar el 80 %. PC1 combina principalmente edad, recencia y consumo, mientras que PC2 está dominada por los tickets de soporte. PCA permitió comprobar que las variables aportan información relativamente diferente y que no conviene forzar una reducción a dos o tres dimensiones.

## Visualización interactiva

La aplicación comunica los resultados principales para público general y está disponible en:

[Aplicación pública en Streamlit](https://pi-mineria-datos-constantinidi-thir-2026.streamlit.app/)

La página EDA contiene exactamente cinco visualizaciones: dos univariadas, dos bivariadas y una multivariada. La página PCA presenta dos visualizaciones: varianza explicada y contribución de las variables a PC1 y PC2. La evidencia técnica completa permanece en los notebooks, el dataset procesado y el log ETL.

## Cómo ejecutar localmente

### 1. Clonar el repositorio

```bash
git clone https://github.com/LeandroConstantinidi/PI_Mineria_Datos_1.git
cd PI_Mineria_Datos_1
```

### 2. Crear el entorno virtual

```powershell
py -m venv .venv
```

### 3. Activar el entorno en PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar las dependencias

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Ejecutar la aplicación

```powershell
python -m streamlit run app/Home.py
```

La aplicación local estará disponible en `http://localhost:8501`.

## Conclusiones

El proceso permitió transformar una base con problemas de calidad en un dataset reproducible de 8.000 usuarios únicos. El plan de suscripción presenta las diferencias descriptivas más claras en el consumo mensual. La edad aislada no permite caracterizar el nivel de visualización y el país no modifica el patrón general entre planes. PCA mostró que las variables numéricas contienen información poco redundante y que no conviene reemplazarlas por solamente dos o tres componentes. Las conclusiones se limitan al dataset analizado y no permiten inferir causalidad ni generalizar automáticamente a otras plataformas.

El desarrollo detallado de las conclusiones se encuentra en [`05_conclusiones.ipynb`](notebooks/05_conclusiones.ipynb) y en el [`informe final`](reports/informe_final.pdf).