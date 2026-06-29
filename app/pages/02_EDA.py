from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="EDA", page_icon="📈", layout="wide")

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "processed" / "streaming_users_clean.csv"
PLAN_ORDER = ["Básico", "Estándar", "Premium"]


@st.cache_data
def cargar_datos() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH, parse_dates=["last_login_date"])


df = cargar_datos()

st.title("Análisis exploratorio")
st.caption("Dos visualizaciones univariadas, dos bivariadas y una multivariada.")

# 1. Univariada: usuarios por plan
st.subheader("1. Usuarios por plan")
conteo_plan = df["subscription_plan"].value_counts().reindex(PLAN_ORDER)
fig, ax = plt.subplots(figsize=(7, 4))
conteo_plan.plot(kind="bar", ax=ax)
ax.set_title("Cantidad de usuarios por plan")
ax.set_xlabel("Plan")
ax.set_ylabel("Usuarios")
ax.tick_params(axis="x", rotation=0)
fig.tight_layout()
st.pyplot(fig)
st.write(
    "**Interpretación:** el plan Básico concentra la mayor cantidad de usuarios, "
    "seguido por Estándar y Premium. Esta composición debe considerarse al leer "
    "los promedios generales."
)

# 2. Univariada: histograma de consumo
st.subheader("2. Distribución del tiempo mensual")
fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(df["monthly_watch_time_mins"], bins=30)
ax.set_title("Distribución del tiempo mensual de visualización")
ax.set_xlabel("Minutos mensuales")
ax.set_ylabel("Usuarios")
fig.tight_layout()
st.pyplot(fig)
st.write(
    f"**Interpretación:** la mediana es {df['monthly_watch_time_mins'].median():.1f} "
    "minutos y la distribución presenta una cola hacia consumos altos. Por eso la "
    "mediana describe mejor al usuario típico que la media."
)

# 3. Bivariada: consumo por plan
st.subheader("3. Tiempo de visualización según el plan")
series = [
    df.loc[df["subscription_plan"] == plan, "monthly_watch_time_mins"]
    for plan in PLAN_ORDER
]
fig, ax = plt.subplots(figsize=(8, 4))
ax.boxplot(series, tick_labels=PLAN_ORDER, showfliers=False)
ax.set_title("Tiempo mensual según el plan")
ax.set_xlabel("Plan")
ax.set_ylabel("Minutos mensuales")
fig.tight_layout()
st.pyplot(fig)
medianas = df.groupby("subscription_plan")["monthly_watch_time_mins"].median()
st.write(
    "**Interpretación:** las medianas aumentan de "
    f"{medianas['Básico']:.1f} minutos en Básico a "
    f"{medianas['Estándar']:.1f} en Estándar y "
    f"{medianas['Premium']:.1f} en Premium. El plan presenta la asociación "
    "descriptiva más clara con el consumo, aunque existe superposición entre grupos."
)

# 4. Bivariada: edad y consumo
st.subheader("4. Edad y tiempo de visualización")
fig, ax = plt.subplots(figsize=(8, 4))
ax.scatter(df["age"], df["monthly_watch_time_mins"], alpha=0.25, s=15)
ax.set_title("Edad y tiempo mensual de visualización")
ax.set_xlabel("Edad")
ax.set_ylabel("Minutos mensuales")
fig.tight_layout()
st.pyplot(fig)
correlacion = df["age"].corr(df["monthly_watch_time_mins"])
st.write(
    f"**Interpretación:** la correlación lineal es {correlacion:.4f}, prácticamente "
    "nula. La edad aislada no permite caracterizar el nivel de consumo."
)

# 5. Multivariada: país, plan y consumo
st.subheader("5. Consumo medio por país y plan")
tabla = df.pivot_table(
    index="country",
    columns="subscription_plan",
    values="monthly_watch_time_mins",
    aggfunc="mean",
).reindex(columns=PLAN_ORDER)
fig, ax = plt.subplots(figsize=(10, 5))
tabla.plot(kind="bar", ax=ax)
ax.set_title("Consumo medio por país y plan")
ax.set_xlabel("País")
ax.set_ylabel("Minutos mensuales promedio")
ax.tick_params(axis="x", rotation=35)
ax.legend(title="Plan")
fig.tight_layout()
st.pyplot(fig)
st.write(
    "**Interpretación:** en los siete países se mantiene el orden general "
    "Premium > Estándar > Básico. El país introduce variaciones, pero no modifica "
    "el patrón principal asociado con el plan."
)
