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

# un contenedor es un elemento que te permite agrupar visualmente otros elementos 
# (widgets, texto, gráficos, etc.) en tu aplicación. 
# Piensa en ellos como cajas o secciones que organizan el contenido.

st.title("📦 Panel de inventario")

##### Estructura con markdown para centrar título
### Interactuar con esta estructura
st.markdown(
    "<h1 style='text-align: center;'> 📦Panel de inventario </h1>", ###Modificar por texto deseado
    unsafe_allow_html=True # Permite a Streamlit interpretar el código HTML y CSS
)

##### Estructura con st.write para centrar título
### Interactuar con esta estructura
st.write(
    "<h1 style='text-align: center;'> 📦 Panel de inventario con st.write </h1>", ###Modificar por texto deseado
    unsafe_allow_html=True # Permite a Streamlit interpretar el código HTML y CSS
)


###### Crear función para centrar cualquier texto
def centered_title(text):
    st.markdown(f"<h1 style='text-align: center;'>{text}</h1>", 
                unsafe_allow_html=True) # Permite a Streamlit interpretar el código HTML y CSS

###Se manda a llamar a la función y como parámetro se le pasa el texto que necesitamos desplegar
centered_title("Título reutilizable centrado") ###Modificar por texto deseado


#####Sección con markdown para crear un contenedor para título con formato
### Interactuar con los parámetros para ver cómo se modifican al renderizar el dashboard
st.markdown(
    """
    <h1 style=' 
        text-align: center;  
        color: #1E3A8A; 
        background-color: #E0F2FE; 
        padding: 20px; 
        border-radius: 15px;
        font-family: "Segoe UI", sans-serif;
        box-shadow: 2px 4px 10px rgba(0,0,0,0.1);
    '>
        📦 Panel de Inventario Avanzado
    </h1>
    """,
    unsafe_allow_html=True # Permite a Streamlit interpretar el código HTML y CSS
)
###Significado de cada línea


#     text-align: center;                      /* Centra el texto en la pantalla */
#     color: #1E3A8A;                          /* Color de fuente azul oscuro, modificarlo con cualquier color en formato hexadecimal
#     background-color: #E0F2FE;               /* Fondo azul claro suave */
#     padding: 20px;                           /* Espacio interno alrededor del texto */
#     border-radius: 15px;                     /* Redondea las esquinas del contenedor */
#     font-family: "Segoe UI", sans-serif;     /* Tipo de letra principal y de respaldo */
#     box-shadow: 2px 4px 10px rgba(0,0,0,0.1);/* Sombra ligera para dar relieve */




st.caption("Clase: contenedores, columnas, métricas y gráficos con datos del socio formador.")

#### Insertar un logo en strealit
#### Agregarle como cadena la liga al logo
st.logo('https://images.squarespace-cdn.com/content/v1/68c0a1903fe42110d35bb3d4/bd9160e8-5fd4-4ee2-8a09-abcec5c0175f/clv_logo_06.png?format=1500w')

#### Insertar una imagen en strealit
#### Agregarle como cadena la liga a la imagen
st.sidebar.image('https://images.squarespace-cdn.com/content/v1/68c0a1903fe42110d35bb3d4/bd9160e8-5fd4-4ee2-8a09-abcec5c0175f/clv_logo_06.png?format=1500w')
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
with st.container(border=True):

    #####Inyectar colores con markdown
    st.markdown("### :blue[1. Resumen ejecutivo]") # blue, green, red, orange, violet, gray, rainbow colores disponibles
    ###########
    st.subheader("1. Resumen ejecutivo")
    st.write("Agrupamos indicadores relacionados dentro de una misma sección visual.")
    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        st.metric("Artículos en la vista", int(len(inventario)))
    with c2:
        unidades = pd.to_numeric(filtrado["existencias"], errors="coerce").fillna(0).sum()
        st.metric("Existencias totales", f"{unidades:,.0f}")
    with c3:
        valor = pd.to_numeric(filtrado["valor_total_inventario"], errors="coerce").fillna(0).sum()
        st.metric("Valor del inventario", f"${valor:,.2f}")

# Contenedor 2: tabla y gráfico en columnas
with st.container(border=True):
    

    st.subheader("2. Detalle de existencias")
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

# Contenedor 3: comparar compras y salidas sin asumir que sus claves coinciden
with st.container(border=True):
    st.subheader("3. Actividad registrada")
    a, b = st.columns(2)
    with a:
        st.markdown("**Compras registradas**")
        st.metric("Registros de compra", len(compras))
        st.metric("Unidades compradas", f"{pd.to_numeric(compras['unidades'], errors='coerce').fillna(0).sum():,.0f}")
    with b:
        st.markdown("**Salidas registradas**")
        st.metric("Registros de salida", len(salidas))
        st.metric("Unidades de salida", f"{pd.to_numeric(salidas['salidas'], errors='coerce').fillna(0).sum():,.0f}")

# Un contenedor de altura fija para mostrar cuándo resulta útil el desplazamiento
with st.container(height=160, border=True):
    st.subheader("4. Notas de interpretación")
    st.write("• No interpretamos compras como demanda ni las salidas como ventas sin validar definiciones.")
    st.write("• Los datos de inventario son un reflejo de la información registrada, no necesariamente del inventario físico.")

# Interacción con estado persistente
with st.container(border=True):
    st.subheader("5. Mini reto: contador de observaciones")
    st.write("Simula el registro de observaciones durante una revisión de inventario.")
    if "observaciones" not in st.session_state:
        st.session_state.observaciones = 0
    x, y = st.columns([1, 3], vertical_alignment="center")
    with x:
        if st.button("➕ Registrar observación", use_container_width=True):
            st.session_state.observaciones += 1
        if st.button("Reiniciar contador", use_container_width=True):
            st.session_state.observaciones = 0
    with y:
        st.metric("Observaciones registradas en esta sesión", st.session_state.observaciones)

st.caption(f"Fuente: {EXCEL.name}. Filas visibles de inventario: {len(filtrado)} de {len(inventario)}.")
