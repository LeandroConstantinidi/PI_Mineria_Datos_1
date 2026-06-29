from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Proyecto Integrador - Minería de Datos I",
    page_icon="📊",
    layout="wide",
)

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "processed" / "streaming_users_clean.csv"
GITHUB_URL = ""


@st.cache_data
def cargar_datos() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH, parse_dates=["last_login_date"])


df = cargar_datos()

st.title("Análisis de usuarios de una plataforma de streaming")
st.subheader("Proyecto Integrador - Minería de Datos I")

st.markdown(
    """
**Integrantes**

- Thir Ferreyra Nadia Lorena
- Constantinidi Leandro Exequiel

**Comisión:** Turno Tarde  
**Fecha de cierre analítico:** 27 de junio de 2026
"""
)

st.markdown(
    """
### Contexto

El proyecto analiza la calidad y los patrones principales de un dataset de
usuarios de una plataforma de streaming. El proceso incluye inspección,
limpieza, análisis exploratorio, escalamiento y PCA. El alcance es descriptivo
y no incluye modelos predictivos.
"""
)

col1, col2, col3 = st.columns(3)
col1.metric("Usuarios finales", f"{len(df):,}".replace(",", "."))
col2.metric("Variables", df.shape[1])
col3.metric("Planes", df["subscription_plan"].nunique())

st.info(
    "La aplicación comunica los resultados principales. La evidencia técnica "
    "completa se encuentra en los notebooks y en el log ETL."
)

if GITHUB_URL:
    st.link_button("Abrir repositorio de GitHub", GITHUB_URL)
else:
    st.caption("El enlace de GitHub se agregará después de publicar el repositorio.")
