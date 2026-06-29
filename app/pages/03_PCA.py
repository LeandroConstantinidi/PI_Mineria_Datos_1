from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="PCA", page_icon="🧭", layout="wide")

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "processed" / "streaming_users_clean.csv"
FECHA_REFERENCIA = pd.Timestamp("2026-06-27")


@st.cache_data
def calcular_pca():
    df = pd.read_csv(DATA_PATH, parse_dates=["last_login_date"])
    df_pca = df.dropna(subset=["last_login_date"]).copy()
    df_pca["days_since_last_login"] = (
        FECHA_REFERENCIA - df_pca["last_login_date"]
    ).dt.days

    variables = [
        "age",
        "monthly_watch_time_mins",
        "customer_support_tickets",
        "days_since_last_login",
    ]

    X = df_pca[variables]
    X_scaled = StandardScaler().fit_transform(X)
    pca = PCA(n_components=len(variables))
    scores = pca.fit_transform(X_scaled)

    variance = pd.DataFrame({
        "Componente": [f"PC{i + 1}" for i in range(len(variables))],
        "Varianza individual (%)": pca.explained_variance_ratio_ * 100,
        "Varianza acumulada (%)": np.cumsum(pca.explained_variance_ratio_) * 100,
    })

    projection = pd.DataFrame(scores[:, :2], columns=["PC1", "PC2"])
    projection["Plan"] = df_pca["subscription_plan"].to_numpy()
    return df, df_pca, variables, variance, projection


df, df_pca, variables, variance, projection = calcular_pca()

st.title("Análisis de Componentes Principales")
st.write(
    "PCA se aplica a edad, minutos mensuales, tickets y días desde el último "
    "ingreso. Las variables se escalan con StandardScaler porque tienen unidades "
    "y rangos diferentes."
)

col1, col2, col3 = st.columns(3)
col1.metric("Usuarios finales", f"{len(df):,}".replace(",", "."))
col2.metric("Usuarios en PCA", f"{len(df_pca):,}".replace(",", "."))
col3.metric("Retención", f"{len(df_pca) / len(df) * 100:.2f} %")

st.caption(
    "Los usuarios sin fecha válida no se incluyen en PCA porque imputar una fecha "
    "habría supuesto inventar información de recencia."
)

# 1. Varianza explicada
st.subheader("1. Varianza explicada")
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(variance["Componente"], variance["Varianza individual (%)"])
ax.plot(
    variance["Componente"],
    variance["Varianza acumulada (%)"],
    marker="o",
)
ax.axhline(80, linestyle="--")
ax.set_title("Varianza explicada por componente")
ax.set_xlabel("Componente")
ax.set_ylabel("Porcentaje")
ax.set_ylim(0, 105)
fig.tight_layout()
st.pyplot(fig)
st.dataframe(variance.round(2), width="stretch")
st.write(
    f"**Interpretación:** PC1 y PC2 explican {variance.loc[1, 'Varianza acumulada (%)']:.2f} % "
    f"y las tres primeras {variance.loc[2, 'Varianza acumulada (%)']:.2f} %. "
    "Para superar el 80 % se necesitan las cuatro componentes; por eso no existe "
    "una reducción eficiente a dos o tres dimensiones."
)

# 2. Proyección PC1-PC2
st.subheader("2. Proyección en PC1 y PC2")
fig, ax = plt.subplots(figsize=(8, 5))
for plan in ["Básico", "Estándar", "Premium"]:
    subset = projection[projection["Plan"] == plan]
    ax.scatter(subset["PC1"], subset["PC2"], alpha=0.25, s=15, label=plan)
ax.set_title("Usuarios proyectados en PC1 y PC2")
ax.set_xlabel(f"PC1 ({variance.loc[0, 'Varianza individual (%)']:.2f} %)")
ax.set_ylabel(f"PC2 ({variance.loc[1, 'Varianza individual (%)']:.2f} %)")
ax.legend(title="Plan")
fig.tight_layout()
st.pyplot(fig)
st.write(
    "**Interpretación:** los grupos se superponen ampliamente. PCA permite observar "
    "la estructura general, pero no clasifica usuarios ni produce grupos claramente separados."
)
