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

    df_pca = df.dropna(
        subset=["last_login_date"]
    ).copy()

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
    pca.fit(X_scaled)

    varianza = pd.DataFrame(
        {
            "Componente": [
                f"PC{i + 1}"
                for i in range(len(variables))
            ],
            "Varianza individual (%)":
                pca.explained_variance_ratio_ * 100,
            "Varianza acumulada (%)":
                np.cumsum(
                    pca.explained_variance_ratio_
                ) * 100,
        }
    )

    cargas = pd.DataFrame(
        pca.components_.T,
        index=variables,
        columns=[
            f"PC{i + 1}"
            for i in range(len(variables))
        ],
    )

    # Los aportes de cada componente suman 100 %.
    contribuciones = (
        cargas[["PC1", "PC2"]].pow(2) * 100
    )

    return (
        df,
        df_pca,
        variables,
        varianza,
        contribuciones,
    )


(
    df,
    df_pca,
    variables,
    varianza,
    contribuciones,
) = calcular_pca()


st.title("Análisis de Componentes Principales")

st.write(
    "PCA se aplica a edad, minutos mensuales, "
    "tickets y días desde el último ingreso. "
    "Las variables se escalan con StandardScaler "
    "porque tienen unidades y rangos diferentes."
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Usuarios finales",
    f"{len(df):,}".replace(",", "."),
)

col2.metric(
    "Usuarios en PCA",
    f"{len(df_pca):,}".replace(",", "."),
)

col3.metric(
    "Retención",
    f"{len(df_pca) / len(df) * 100:.2f} %",
)

st.caption(
    "Los usuarios sin fecha válida no se incluyen "
    "en PCA porque imputar una fecha habría supuesto "
    "inventar información de recencia."
)


# 1. Varianza explicada
st.subheader("1. Varianza explicada")

fig, ax = plt.subplots(figsize=(7, 4))

ax.bar(
    varianza["Componente"],
    varianza["Varianza individual (%)"],
)

ax.plot(
    varianza["Componente"],
    varianza["Varianza acumulada (%)"],
    marker="o",
)

ax.axhline(80, linestyle="--")

ax.set_title(
    "Varianza explicada por componente"
)

ax.set_xlabel("Componente")
ax.set_ylabel("Porcentaje")
ax.set_ylim(0, 105)

fig.tight_layout()
st.pyplot(fig)

st.dataframe(
    varianza.round(2),
    width="stretch",
)

st.write(
    f"**Interpretación:** PC1 y PC2 explican "
    f"{varianza.loc[1, 'Varianza acumulada (%)']:.2f} % "
    f"y las tres primeras "
    f"{varianza.loc[2, 'Varianza acumulada (%)']:.2f} %. "
    "Para superar el 80 % se necesitan las cuatro "
    "componentes; por eso no existe una reducción "
    "eficiente a dos o tres dimensiones."
)


# 2. Contribución de las variables
st.subheader(
    "2. ¿Qué variables forman PC1 y PC2?"
)

nombres = {
    "age": "Edad",
    "monthly_watch_time_mins":
        "Minutos mensuales",
    "customer_support_tickets":
        "Tickets de soporte",
    "days_since_last_login":
        "Días desde el último ingreso",
}

aportes = contribuciones.rename(index=nombres)

y = np.arange(len(aportes))
alto = 0.34

fig, ax = plt.subplots(figsize=(8, 5))

ax.barh(
    y - alto / 2,
    aportes["PC1"],
    height=alto,
    label="PC1",
)

ax.barh(
    y + alto / 2,
    aportes["PC2"],
    height=alto,
    label="PC2",
)

ax.set_yticks(y)
ax.set_yticklabels(aportes.index)
ax.invert_yaxis()

ax.set_xlim(0, 100)
ax.set_xlabel("Contribución relativa (%)")

ax.set_title(
    "Aporte de cada variable a las "
    "dos primeras componentes"
)

ax.legend()
ax.grid(axis="x", alpha=0.25)

for indice, valor in enumerate(
    aportes["PC1"]
):
    ax.text(
        valor + 1,
        indice - alto / 2,
        f"{valor:.1f} %",
        va="center",
        fontsize=9,
    )

for indice, valor in enumerate(
    aportes["PC2"]
):
    ax.text(
        valor + 1,
        indice + alto / 2,
        f"{valor:.1f} %",
        va="center",
        fontsize=9,
    )

fig.tight_layout()
st.pyplot(fig)

pc1_orden = aportes["PC1"].sort_values(
    ascending=False
)

pc2_orden = aportes["PC2"].sort_values(
    ascending=False
)

st.write(
    f"**Interpretación:** PC1 combina principalmente "
    f"**{pc1_orden.index[0]}** "
    f"({pc1_orden.iloc[0]:.1f} %), "
    f"**{pc1_orden.index[1]}** "
    f"({pc1_orden.iloc[1]:.1f} %) y "
    f"**{pc1_orden.index[2]}** "
    f"({pc1_orden.iloc[2]:.1f} %). "
    f"PC2 está dominada por "
    f"**{pc2_orden.index[0]}** "
    f"({pc2_orden.iloc[0]:.1f} %). "
    "Esto muestra que las variables aportan "
    "información diferente y ayuda a explicar "
    "por qué PCA no logra resumirlas eficientemente "
    "en solo dos componentes."
)

st.caption(
    "Las contribuciones se calculan a partir del "
    "cuadrado de las cargas del PCA. Por eso, los "
    "aportes de las variables suman 100 % dentro "
    "de cada componente."
)