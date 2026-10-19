from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Abasto Inteligente | Panel", 
    page_icon="📦", 
    layout="wide")

DATA_PATH = Path(__file__).resolve().parents[0] / "datos" / "Datos_CLV_2026_Tec_v2.xlsx"
sheet_name="Existencias_04_09_2026"

@st.cache_data
def cargar_archivo():
    return pd.read_excel(DATA_PATH, sheet_name=sheet_name)


st.title("📦 Abasto Inteligente")
st.caption("Prototipo de consulta de inventario y movimientos de almacén.")

try:
    inventario = cargar_hoja("Existencias_04_09_2026")
except Exception as error:
    st.error(f"No se pudo leer el archivo: {error}")
    st.stop()



inventario["existencias"] = pd.to_numeric(inventario["existencias"], errors="coerce")
inventario["valor_total_inventario"] = pd.to_numeric(inventario["valor_total_inventario"], errors="coerce")

# Controles agrupados en la barra lateral
st.sidebar.title("Filtros de consulta")
buscar = st.sidebar.text_input("Buscar artículo")
marcas = sorted(inventario["marca"].dropna().astype(str).unique().tolist())
marca = st.sidebar.selectbox("Marca", ["Todas"] + marcas)
almacenes = sorted(inventario["nombre_almacen"].dropna().astype(str).unique().tolist())
almacen = st.sidebar.selectbox("Almacén", ["Todos"] + almacenes)


dff = inventario.copy()



st.subheader("Lista de revisión")
st.dataframe(dff.sort_values("existencias", na_position="first"),
             use_container_width=True)




st.markdown("""
- Existencia baja es una **señal para revisar**, no una orden automática de compra.
- Para calcular punto de reorden hacen falta demanda/consumo confiable, plazo de entrega, stock de seguridad y políticas por artículo.
- Las ventas negadas de CRM no deben atribuirse a un artículo si no existe una clave que las conecte con `articulo_id`.
""")
