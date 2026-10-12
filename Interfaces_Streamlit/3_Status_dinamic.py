import streamlit as st
import time
from random import choice, randint


# Título
st.title("🚀 Simulador de Operaciones: ¡Supervivencia en el Hot Sale!")
st.write(
    "¡Bienvenidos, Ingenieros de Cadena de Suministro! Están a cargo del CEDIS "
    "más grande del país durante la hora pico del Hot Sale. Cada clic simula un "
    "evento en tiempo real. ¿Podrán mantener la operación a flote?"
)

# SECCIÓN 1: Botón de interacción para iniciar el día
st.header("🎛️ Consola de Control Central")
boton_monitoreo = st.button("🔄 Escanear estado de la Red de Suministro")

# Si el alumno presiona el botón, se detona la simulación emocionante
if boton_monitoreo:
    st.subheader("📊 Diagnóstico del Sistema en Tiempo Real")
    time.sleep(1.2)
    # 1. ÉXITO (Simula un proceso logístico optimizado)
    st.success("✅ **¡Ruta de Entrega Optimizada!** Los camiones de última milla salieron a tiempo. Tiempo de ciclo reducido en un 15%.")
    time.sleep(1.2)
    # 2. INFORMACIÓN (Aviso operativo de almacén)
    st.info("ℹ️ **Aviso de Embarques:** Se reporta la llegada de 3 contenedores marítimos al puerto de Manzanillo para el inventario de contingencia.")
    time.sleep(1.2)
    # 3. ADVERTENCIA (Un problema clásico de stock que requiere atención)
    st.warning("⚠️ **¡Alerta de Stockout Próximo!** El *Producto Estrella A* tiene alta demanda. El inventario restante solo cubrirá las próximas 2 horas.")
    time.sleep(1.2)
    # 4. ERROR (Una crisis total en la cadena que detiene la operación)
    st.error("🚨 **¡Quiebre de Operación!** El sistema de bandas transportadoras en la Zona B se ha detenido. Los pedidos hacia el norte del país están varados.")

    

else:
    # Estado inicial antes de que interactúen
    st.info("💡 Haz clic en el botón superior para encender los servidores de monitoreo y recibir los reportes de los supervisores.")


# Pie de página académico
st.caption(
    " Prototipo de Control de Operaciones v1.2 | Analítica de datos."
)

