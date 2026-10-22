from pathlib import Path
import pandas as pd
import streamlit as st


st.set_page_config(page_title="Abasto inteligente | Análisis", page_icon="📦", layout="wide")

DATA_PATH = Path(__file__).resolve().parents[0] / "Datos" / "Datos_CLV_2026_Tec_v2.xlsx"
SHEET_NAMES = [
    "Existencias_04_09_2026",
    "Salidas_Almacen",
    "Histórico_Compras",
    "Clasificación_Articulos"
]

@st.cache_data
def cargar_hojas(nombre_hoja):
    return pd.read_excel(DATA_PATH, sheet_name=list(SHEET_NAMES))


st.title("📦 Abasto inteligente")
st.caption("Pestañas para explorar datos relacionados por artículo")

try:
    hojas = cargar_hojas(DATA_PATH)
except (FileNotFoundError, ValueError, OSError) as error:
    st.error(f"No fue posible cargar las hojas de {DATA_PATH.name}: {error}")
    st.stop()


inventario = hojas["Existencias_04_09_2026"].copy()
salidas = hojas["Salidas_Almacen"].copy()
compras = hojas["Histórico_Compras"].copy()
clasificacion = hojas["Clasificación_Articulos"].copy()


st.info(
    "Las pestañas muestran cada fuente por separado y permiten explorar cómo se relacionan por artículo."
)



inventario["estado_revision"] = "Por encima del umbral"
inventario.loc[
    inventario["existencias"].notna() & (inventario["existencias"] <= umbral),
    "estado_revision",
] = "Revisar existencia"
inventario.loc[inventario["existencias"].isna(), "estado_revision"] = (
    "Revisar calidad del dato"
)


st.warning(
    "Este tablero ayuda a explorar y revisar información. No pronostica demanda ni "
    "recomienda cantidades o fechas de compra."
)
