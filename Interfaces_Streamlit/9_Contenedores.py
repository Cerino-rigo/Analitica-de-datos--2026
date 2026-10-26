from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Inventario | Contenedores", page_icon="📦", layout="wide")

EXCEL = Path(__file__).resolve().parents[0] / "Datos" / "Datos_CLV_2026_Tec_v2.xlsx"

@st.cache_data
def cargar_datos(ruta):
    # Carga únicamente las hojas que se usan
    inventario = pd.read_excel(ruta, sheet_name="Existencias_04_09_2026")
    compras = pd.read_excel(ruta, sheet_name="Histórico_Compras")
    salidas = pd.read_excel(ruta, sheet_name="Salidas_Almacen")
    return inventario, compras, salidas

try:
    inventario, compras, salidas = cargar_datos(EXCEL)
except Exception as exc:
    st.error(f"No fue posible leer el Excel: {exc}")
    st.stop()


st.title("📦 Panel de inventario")


st.caption("Clase: contenedores, columnas, métricas y gráficos con datos del socio formador.")

st.sidebar.header("Filtros de la vista")
marcas = sorted(inventario["marca"].dropna().astype(str).unique().tolist())
marca = st.sidebar.selectbox("Marca", ["Todas"] + marcas)
almacenes = sorted(inventario["nombre_almacen"].dropna().astype(str).unique().tolist())
almacen = st.sidebar.selectbox("Almacén", ["Todos"] + almacenes)
umbral = st.sidebar.number_input(
    "Umbral  (unidades)",
    min_value=0,
    value=5,
    step=1,
    help="Se usa para practicar el diseño de la interfaz; no es un punto de reorden.",
)
inventario["existencias"] = pd.to_numeric(inventario["existencias"], errors="coerce")
inventario["valor_total_inventario"] = pd.to_numeric(
    inventario["valor_total_inventario"], errors="coerce"
)

filtrado = inventario.copy()
if marca != "Todas":
    filtrado = filtrado[filtrado["marca"].astype(str) == marca]
if almacen != "Todos":
    filtrado = filtrado[filtrado["nombre_almacen"].astype(str) == almacen]

bajo_umbral = filtrado["existencias"].notna() & (filtrado["existencias"] <= umbral)
unidades = filtrado["existencias"].sum(min_count=1)
valor = filtrado["valor_total_inventario"].sum(min_count=1)

# Contenedor 1: encabezado y métricas


# Contenedor 2: tabla y gráfico en columnas

izquierda, derecha = st.columns([0.58, 0.42], gap="large", vertical_alignment="top")
with izquierda:
    st.markdown("**Tabla filtrada**")
    st.metric("Valor total registrado", f"${valor:,.2f}" if pd.notna(valor) else "N/D")
    if filtrado.empty:
        st.info("No hay registros para los filtros seleccionados.")
    else:
        detalle = filtrado.copy()
        detalle["estado_revision"] = "Por encima del umbral"
        detalle.loc[bajo_umbral, "estado_revision"] = "Revisar existencia"
        detalle.loc[detalle["existencias"].isna(), "estado_revision"] = (
            "Revisar calidad del dato"
        )
        st.dataframe(
            detalle.sort_values("existencias", na_position="first"),
            hide_index=True,
            use_container_width=True,
        )
with derecha:
    st.markdown("**Existencias por artículo**")
    if not filtrado.empty:
        fig = px.bar(
            filtrado, x="nombre_articulo", y="existencias", color="nombre_almacen",
            title="Existencias registradas", labels={"nombre_articulo": "Artículo", "existencias": "Unidades", "nombre_almacen": "Almacén"}
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Selecciona al menos un almacén en la barra lateral.")

# Contenedor 3: comparar compras y salidas


# Un contenedor de altura fija para mostrar cuándo resulta útil el desplazamiento

st.subheader("4. Notas de interpretación")
st.write("• No interpretamos compras como demanda ni las salidas como ventas sin validar definiciones.")
st.write("• Los datos de inventario son un reflejo de la información registrada, no necesariamente del inventario físico.")

# Interacción con estado persistente

st.subheader("5. Mini reto: contador de observaciones")
st.write("Simula el registro de observaciones durante una revisión de inventario.")

x, y = st.columns([1, 3], vertical_alignment="center")
with x:
    if st.button("➕ Registrar observación", use_container_width=True):
        pass
    if st.button("Reiniciar contador", use_container_width=True):
        pass
with y:
    st.metric("Observaciones registradas en esta sesión", 0)

st.caption(f"Fuente: {EXCEL.name}. Filas visibles de inventario: {len(filtrado)} de {len(inventario)}.")
