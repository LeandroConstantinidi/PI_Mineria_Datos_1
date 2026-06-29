from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dataset", page_icon="🗂️", layout="wide")

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "processed" / "streaming_users_clean.csv"
LOG_PATH = ROOT / "logs" / "pipeline_log.csv"


@st.cache_data
def cargar_archivos():
    datos = pd.read_csv(DATA_PATH, parse_dates=["last_login_date"])
    log = pd.read_csv(LOG_PATH)
    return datos, log


df, log_etl = cargar_archivos()

st.title("Dataset y calidad de datos")
st.write(
    "Cada fila representa un usuario. La base incluye edad, plan, consumo "
    "mensual, país, género favorito, último ingreso y tickets de soporte."
)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Usuarios", f"{len(df):,}".replace(",", "."))
col2.metric("Variables", df.shape[1])
col3.metric("IDs repetidos", int(df["user_id"].duplicated().sum()))
col4.metric("Fechas faltantes", int(df["last_login_date"].isna().sum()))

st.subheader("Vista previa")
st.dataframe(df.head(10), width="stretch")

st.subheader("Transformaciones principales")
st.markdown(
    """
- Se conservó la primera aparición de cada identificador repetido.
- Se unificaron planes, países y géneros escritos de distintas formas.
- Las edades incompatibles con la distribución observada se imputaron con la mediana.
- Los minutos imposibles se imputaron con la mediana de cada plan.
- Los códigos inválidos de tickets se imputaron con la mediana.
- Las fechas ambiguas, imposibles o futuras permanecieron como faltantes.
"""
)

st.subheader("Log ETL")
st.dataframe(log_etl, width="stretch")
