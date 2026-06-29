import streamlit as st

st.set_page_config(page_title="Conclusiones", page_icon="✅", layout="wide")

st.title("Conclusiones")

st.subheader("Hallazgos principales")
st.markdown(
    """
- El plan de suscripción presenta la asociación descriptiva más clara con el consumo mensual.
- Las medianas aumentan de Básico a Estándar y Premium.
- La edad no muestra una relación lineal relevante con los minutos de visualización.
- El orden Premium > Estándar > Básico se mantiene en los siete países.
- PCA no logra reducir eficientemente las cuatro variables seleccionadas.
"""
)

st.subheader("Alcance")
st.success(
    "Los resultados describen asociaciones presentes en este dataset. No permiten "
    "afirmar que el plan cause mayor consumo ni generalizar automáticamente a otras plataformas."
)

st.subheader("Limitaciones")
st.markdown(
    """
- No se conoce el procedimiento de muestreo ni la población total.
- Faltan variables como precio, antigüedad, dispositivos, renovaciones y cancelaciones.
- Las imputaciones conservan usuarios, pero introducen incertidumbre.
- Permanecen fechas desconocidas porque no podían reconstruirse con seguridad.
- La correlación y PCA resumen principalmente relaciones lineales.
"""
)

st.subheader("Próximos pasos")
st.markdown(
    """
- Incorporar documentación del origen y del período de los datos.
- Agregar variables comerciales, temporales y de comportamiento.
- Validar rangos, categorías y fechas al momento de registrar la información.
- Comparar otras estrategias de imputación si el objetivo futuro lo requiere.
"""
)
