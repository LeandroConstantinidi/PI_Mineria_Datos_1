from pathlib import Path

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Proyecto Integrador - Minería de Datos I",
    page_icon="📊",
    layout="wide",
)


# Rutas del proyecto
ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = (
    ROOT
    / "data"
    / "processed"
    / "streaming_users_clean.csv"
)


# Enlaces públicos
GITHUB_URL = (
    "https://github.com/"
    "LeandroConstantinidi/PI_Mineria_Datos_1"
)

STREAMLIT_URL = (
    "https://pi-mineria-datos-"
    "constantinidi-thir-2026.streamlit.app/"
)


@st.cache_data
def cargar_datos() -> pd.DataFrame:
    """Carga el dataset procesado utilizado en el proyecto."""
    return pd.read_csv(
        DATA_PATH,
        parse_dates=["last_login_date"],
    )


df = cargar_datos()


# Encabezado
st.title(
    "Análisis de usuarios de una plataforma de streaming"
)

st.subheader(
    "Proyecto Integrador - Minería de Datos I"
)


# Información general
st.markdown(
    """
**Integrantes**

- Thir Ferreyra Nadia Lorena
- Constantinidi Leandro Exequiel

**Carrera:** Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial  
**Comisión:** Turno Tarde  
**Fecha de cierre analítico:** 27 de junio de 2026
"""
)


# Contexto
st.markdown(
    """
### Contexto

El proyecto analiza la calidad y los patrones principales de un
dataset de usuarios de una plataforma de streaming.

El proceso incluye inspección inicial, limpieza y preparación de
datos, análisis exploratorio, escalamiento y reducción de
dimensionalidad mediante PCA.

El alcance es descriptivo y exploratorio. No se desarrollan modelos
predictivos ni se establecen relaciones causales.
"""
)


# Métricas principales
col1, col2, col3 = st.columns(3)

col1.metric(
    "Usuarios finales",
    f"{len(df):,}".replace(",", "."),
)

col2.metric(
    "Variables",
    df.shape[1],
)

col3.metric(
    "Planes",
    df["subscription_plan"].nunique(),
)


st.info(
    "La aplicación comunica los resultados principales para público "
    "general. La evidencia técnica completa se encuentra en los "
    "notebooks, el dataset procesado y el log ETL."
)


# Enlaces públicos
st.subheader("Enlaces del proyecto")

col_github, col_streamlit = st.columns(2)

with col_github:
    st.markdown(
        """
        **Repositorio público**

        Contiene los datos, notebooks, aplicación, informe final
        y registro del proceso ETL.
        """
    )

    st.link_button(
        "Abrir repositorio de GitHub",
        GITHUB_URL,
    )


with col_streamlit:
    st.markdown(
        """
        **Aplicación pública**

        Permite consultar el dataset, el análisis exploratorio,
        PCA y las conclusiones.
        """
    )

    st.link_button(
        "Abrir aplicación en Streamlit",
        STREAMLIT_URL,
    )


st.caption(
    "Proyecto académico desarrollado para la asignatura "
    "Minería de Datos I."
)