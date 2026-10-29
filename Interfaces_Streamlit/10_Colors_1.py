import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Demo de personalización en Streamlit",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 Guía de personalización y color en Streamlit")
st.write("Este script compara los diferentes métodos disponibles para estilizar componentes.")


# MÉTODO 2: CONFIGURACIÓN DE CSS GLOBAL

# Inyectamos el CSS global al principio para que las clases estén disponibles
st.markdown("""
    <style>
    .titulo-avanzado-css {
        text-align: center; 
        color: #1E3A8A; 
        background-color: #E0F2FE; 
        padding: 20px; 
        border-radius: 15px;
        font-family: 'Segoe UI', sans-serif;
        box-shadow: 2px 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)



# INTERFAZ EN COLUMNAS PARA COMPARACIÓN

col1, col2, col3 = st.columns(3)

# COLUMNA 1: MÉTODO TRADICIONAL (HTML INLINE)
with col1:
    st.subheader("1. HTML Inline (Tradicional)")
    
    # Ejemplo básico
    st.markdown("<h1 style='text-align: center;'>📦 Panel</h1>", unsafe_allow_html=True)
    
    # Ejemplo con función reutilizable
    def centered_title(text):
        st.markdown(f"<h3 style='text-align: center; color: #FF5733;'>{text}</h3>", unsafe_allow_html=True)
    
    centered_title("Título Reutilizable")
    
    st.info(
        "💡 **Nota técnica:** Permite un control rápido y local. "
        "Sin embargo, mezclar estructura y diseño directamente en el string "
        "puede volverse difícil de mantener si la app crece."
    )

# COLUMNA 2: CSS GLOBAL (SEPARACIÓN DE ESTILOS) 
with col2:
    st.subheader("2. Clases CSS Globales")
    
    # Renderizado usando la clase declarada al inicio del script
    st.markdown("<div class='titulo-avanzado-css'>📦 Inventario Avanzado</div>", unsafe_allow_html=True) #Se llama al formato declarado arriba y se agrega el texto deseado
    st.markdown("<div class='titulo-avanzado-css'>📊 Reporte de Ventas</div>", unsafe_allow_html=True)
    
    st.success(
        "💡 **Nota técnica:** Es la mejor práctica cuando usas HTML. "
        "Separa la lógica de diseño de los datos. Cambiar el color de fondo "
        "en el bloque `<style>` actualizará automáticamente todos los títulos."
    )

# COLUMNA 3: ENFOQUE NATIVO MODERNO (RECOMENDADO) 

with col3:
    st.subheader("3. Componentes Nativos")
    
    with st.container(border=True):
        st.markdown("### :blue[📦 Panel de Inventario Nativo]")
        st.markdown("Este texto tiene fondo resaltado: :blue-background[Texto Destacado]")
        st.caption("Contenido dentro del contenedor estilizado nativamente.")
        
    with st.container(border=True):
        st.markdown("### :violet[🌈 Paleta Arcoíris Nativa]")
        st.markdown("También puedes usar colores fijos como :red[Rojo], :orange[Naranja] o :rainbow[Arcoíris].")

    st.warning(
        "💡 **Nota técnica:** **No requiere** `unsafe_allow_html=True`. "
        "Es completamente seguro frente a ataques XSS y tiene la enorme ventaja de "
        "adaptarse de forma automática si el usuario cambia entre Modo Claro y Oscuro."
    )

