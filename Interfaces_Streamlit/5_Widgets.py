import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Clase interactiva | Widgets", 
    layout="wide")

DATA_PATH = Path(__file__).resolve().parents[0] / "datos" / "Datos_CLV_2026_Tec_v2.xlsx"
sheet_name="Existencias_04_09_2026"

@st.cache_data
def cargar_archivo():
    return pd.read_excel(DATA_PATH, sheet_name=sheet_name)

st.title("Widgets para explorar artículos")
st.caption("Los filtros son herramientas de consulta. Los widgets modifican variables de Python.")

try:
    df = cargar_archivo()
except Exception as error:
    st.error(f"No se pudo leer el archivo: {error}")
    st.stop()



st.subheader("Filtros de Búsqueda Avanzada")
# Widget 1: búsqueda de texto
buscar = st.text_input("🔍 Buscar por ID o nombre de artículo")
# Widget 2: selectbox
almacenes = sorted(df["nombre_almacen"].dropna().astype(str).unique().tolist())
#almacen = st.selectbox("🏬 Almacén (Muestra selección obligatoria)", ["Todos"] + almacenes)
almacen = st.selectbox("🏬 Almacén (Muestra selección obligatoria)", almacenes) #presentamos primero este ejemplo, sin todos, para mostrar que no hay opción de "ninguno" en selectbox. Luego mostrar la versión con "Todos" como opción.
#Widget 3: multiselect
marcas = sorted(df["marca"].dropna().astype(str).unique().tolist())
marca = st.multiselect("🏷️ Filtrar por Marca(s)", marcas, placeholder="Todas las marcas")

#Widget 5: slider
#Sintáxis de slider: st.slider(label, min_value, max_value, value=None, step=None, format=None, key=None)
 # Dinamismo del Slider: Calculado de manera segura
max_existencias = int(max(1, df["existencias"].max(skipna=True) or 1))
rango = st.slider("📦 Rango de existencias en almacén", 0, max_existencias, (0, max_existencias))

# Widget 6: checkbox
# Checkbox para alertas de desabasto crítico
solo_alertas = st.checkbox("⚠️ Mostrar solo artículos en umbral crítico (Q25)")

# PROCESAMIENTO DE FILTROS

filtrado = df.copy()
if buscar.strip():
    patron = buscar.strip()
    coincide =(
        filtrado["nombre_articulo"].astype(str).str.contains(patron, case=False, na=False) 
        | filtrado["articulo_id"].astype(str).str.contains(patron, case=False, na=False)
    )
    filtrado = filtrado[coincide]


if marca: 
    filtrado = filtrado[filtrado["marca"].astype(str).isin(marca)]

#if almacen != "Todos":
if almacen: #Presentar primero este ejemplo, sin todos, para mostrar que no hay opción de "ninguno" en selectbox. Luego mostrar la versión con "Todos" como opción.

    filtrado = filtrado[filtrado["nombre_almacen"].astype(str) == almacen]

mask_rango = filtrado["existencias"].between(rango[0], rango[1], inclusive="both")
if solo_alertas:
    umbral_critico = filtrado["existencias"].quantile(0.25)
    mask_rango = mask_rango & (filtrado["existencias"] <= umbral_critico)
filtrado = filtrado[mask_rango]

st.subheader("Resultados de la consulta")

st.metric("Artículos/filas coincidentes", f"{len(filtrado):,}")
st.metric("Existencias promedio", "N/D" if filtrado["existencias"].dropna().empty else f"{filtrado['existencias'].mean():,.2f} ")

st.dataframe(filtrado, use_container_width=True)

st.download_button("Exportar resultados filtrados", 
                    filtrado.to_csv(index=False).encode("utf-8-sig"),
                    "existencias_filtradas.csv",
                    "text/csv")
