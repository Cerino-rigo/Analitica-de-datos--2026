# 'yield' se utiliza para crear funciones generadoras. Estas funciones, a diferencia 
# de las funciones regulares con 'return', retornan una secuencia de valores uno a la vez,
#  sin almacenar toda la secuencia en memoria. Esto es especialmente útil para iterar 
# sobre grandes conjuntos de datos o secuencias infinitas
import time
import numpy as np 
import pandas as pd 
import streamlit as st



def stream_data():
    # Mensaje 1: Introducción narrativa
    intro_text = (
        "🤖 **Asistente de IA:** ¡Hola! Estoy procesando los datos de ventas de la última semana. "
        "He generado una matriz aleatoria que simula el rendimiento de 10 productos diferentes "
        "durante los últimos 5 días. Aquí tienes el reporte preliminar:\n\n"
    )
   
        
    #  yield, palabra clave que convierte una función en un generador, el cual pausa su ejecución 
    # para devolver un valor y recuerda su estado para continuar desde el mismo punto en la siguiente llamada

    
    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["Prod A", "Prod B", "Prod C", "Prod D", "Prod E", "Prod F", "Prod G", "Prod H", "Prod I", "Prod J"]
        
    )
    

def stream_reporte():

    # Mensaje 2: Conclusión o insights
    conclusion_text = (
        "\n\n💡 **Análisis rápido:** Como puedes observar, los valores fluctúan alrededor de cero "
        "(distribución normal). Los números positivos representan días con ganancias sobre la media, "
        "mientras que los negativos alertan sobre posibles caídas de stock. "
        "¡Espero que esta simulación te sea de utilidad para la clase!"
    )
    

st.title("🔄 Simulación de análisis en tiempo real")

