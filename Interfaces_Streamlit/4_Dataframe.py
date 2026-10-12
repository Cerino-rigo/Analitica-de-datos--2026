from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Inventario | DataFrames", 
    page_icon="📦", 
    layout="wide",
    
    )
#La línea de código construye una ruta absoluta hacia el archivo Estructura_datos.xlsx (ubicado dentro de una carpeta llamada datos) tomando como referencia la ubicación del script actual en el que se está escribiendo.
# Se usa la librería pathlib de Python y se desglosa de la siguiente manera:
# • Path(__file__): Obtiene la ruta del archivo de código (.py) que se está ejecutando actualmente.
# • .resolve(): Convierte esa ruta en una ruta absoluta y limpia, eliminando accesos directos (symlinks) o referencias ambiguas.
# • .parents[1]: Sube dos niveles en el árbol de directorios a partir del archivo actual:
# 	• .parents[0] (o .parent) es la carpeta directa donde está el script.
# 	• .parents[1] es la carpeta que contiene a esa carpeta (el "abuelo" o dos niveles arriba).
DATA_PATH = Path(__file__).resolve().parents[0] / "Datos" / "Datos_CLV_2026_Tec_v2.xlsx"


st.title("📦 Abasto Inteligente")
st.header("1. Consulta del inventario")
st.markdown(
    "En esta primera versión exploraremos la tabla de existencias. "
    "Todavía no se generan recomendaciones reales de compra."
)



st.caption(f"Archivo de práctica: {DATA_PATH.name} | Hoja: {sheet_name}")

st.write("Columnas disponibles:", list(df.columns))


st.subheader("Inventario disponible")




st.info(
    "Nota: el archivo de estructura compartido contiene solo una muestra pequeña. "
    "Los umbrales de inventario y cualquier futura recomendación deberán validarse con la empresa."
)

