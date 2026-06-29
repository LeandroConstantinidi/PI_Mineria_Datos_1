# Proyecto Integrador de Minería de Datos I

## Información general

| Campo                    | Detalle                                                            |
| ------------------------ | ------------------------------------------------------------------ |
| **Título**               | Análisis de usuarios de una plataforma de streaming                |
| **Carrera**              | Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial |
| **Asignatura**           | Minería de Datos I                                                 |
| **Comisión**             | Turno Tarde                                                        |
| **Profesor**             | Fernando Elías Mubarqui                                            |
| **Integrantes**          | Thir Ferreyra Nadia Lorena<br>Constantinidi Leandro Exequiel       |
| **Fuente**               | Dataset provisto por la cátedra                                    |
| **Fecha de elaboración** | Junio de 2026                                                      |

## Enlaces públicos

* [Repositorio público de GitHub](https://github.com/LeandroConstantinidi/PI_Mineria_Datos_1)
* [Aplicación pública en Streamlit](https://pi-mineria-datos-constantinidi-thir-2026.streamlit.app/)
* [Informe final en PDF](reports/informe_final.pdf)
* [Registro del proceso ETL](logs/pipeline_log.csv)

## Objetivo del proyecto

El objetivo del proyecto es desarrollar un proceso reproducible de inspección, preparación, análisis exploratorio y reducción de dimensionalidad sobre un dataset de usuarios de una plataforma de streaming.

El alcance es descriptivo y exploratorio. No se desarrollan modelos predictivos ni se establecen relaciones causales.

## Dataset

El archivo original contiene información sobre usuarios, edad, plan de suscripción, tiempo mensual de visualización, país, género favorito, fecha del último ingreso y tickets de soporte.

El dataset original se conserva sin modificaciones en:

[`data/raw/streaming_users_dirty.json`](data/raw/streaming_users_dirty.json)

El dataset preparado para el análisis se encuentra en:

[`data/processed/streaming_users_clean.csv`](data/processed/streaming_users_clean.csv)

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

## Desarrollo del análisis

El trabajo se organizó en cinco notebooks ejecutados y documentados.

### 1. Inspección inicial

La revisión de la estructura, los tipos de datos, los valores faltantes, los duplicados y las inconsistencias iniciales se encuentra en:

[`01_inspeccion_inicial.ipynb`](notebooks/01_inspeccion_inicial.ipynb)

### 2. Calidad y limpieza de datos

Las reglas de validación, normalización, tratamiento de valores incompatibles, imputaciones y generación del dataset procesado se documentan en:

[`02_calidad_y_limpieza.ipynb`](notebooks/02_calidad_y_limpieza.ipynb)

### 3. Análisis exploratorio

El análisis univariado, bivariado y multivariado se desarrolla en:

[`03_eda.ipynb`](notebooks/03_eda.ipynb)

Las visualizaciones seleccionadas para público general están disponibles en la sección EDA de la aplicación Streamlit.

### 4. Reducción de dimensionalidad

El escalamiento de variables y el análisis de componentes principales se documentan en:

[`04_pca.ipynb`](notebooks/04_pca.ipynb)

Las visualizaciones seleccionadas para comunicar el procedimiento están disponibles en la sección PCA de la aplicación Streamlit.

### 5. Conclusiones

Las conclusiones, limitaciones y recomendaciones se desarrollan en:

[`05_conclusiones.ipynb`](notebooks/05_conclusiones.ipynb)

La síntesis formal del proyecto se encuentra en:

[`reports/informe_final.pdf`](reports/informe_final.pdf)

## Trazabilidad del proceso ETL

Las transformaciones realizadas durante la preparación de los datos y su impacto sobre el dataset se registraron en:

[`logs/pipeline_log.csv`](logs/pipeline_log.csv)

Este archivo permite consultar la secuencia de decisiones aplicada durante el proceso de limpieza y preparación.

## Aplicación interactiva

La aplicación pública permite consultar:

* La descripción del proyecto.
* El dataset procesado y su calidad.
* Las visualizaciones del análisis exploratorio.
* El análisis de componentes principales.
* Las conclusiones y limitaciones.

Acceso público:

[Aplicación en Streamlit Cloud](https://pi-mineria-datos-constantinidi-thir-2026.streamlit.app/)

## Cómo ejecutar la aplicación localmente

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

Si PowerShell bloquea la activación, ejecutar primero:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Luego activar nuevamente:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar las dependencias

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Ejecutar Streamlit

```powershell
python -m streamlit run app/Home.py
```

La aplicación local estará disponible en:

```text
http://localhost:8501
```

Para detener la aplicación:

```text
Ctrl + C
```

## Consulta de resultados

El README funciona como guía de navegación y reproducción del proyecto. Los resultados y sus interpretaciones deben consultarse en los siguientes entregables:

* [Aplicación pública en Streamlit](https://pi-mineria-datos-constantinidi-thir-2026.streamlit.app/)
* [`03_eda.ipynb`](notebooks/03_eda.ipynb)
* [`04_pca.ipynb`](notebooks/04_pca.ipynb)
* [`05_conclusiones.ipynb`](notebooks/05_conclusiones.ipynb)
* [Informe final en PDF](reports/informe_final.pdf)
