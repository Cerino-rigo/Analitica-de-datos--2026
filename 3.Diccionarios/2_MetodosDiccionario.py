# Diccionario de ejemplo 
# Supongamos que es un mapeo: identificador de muestra -> valor medido (por ejemplo, concentración)
datos = {
    "muestra_id": 101,       # identificador de la muestra
    "valor_medido": 2.5,      # valor de la medición (por ejemplo, concentración)
    "unidad": "mg/L",          # unidad de la medición
    "control": False,           # indicador de si es una muestra de control
    "etapa_proceso": "filtrado" # etapa del proceso en la que se tomó la medición
}


# Eliminar datos del diccionario
# - Usamos pop para eliminar una clave y opcionalmente obtener su valor
valor_eliminado = datos.pop("valor_medido", None)  # None si no existe la clave



# - También se puede eliminar con del
del datos["muestra_id"]




# Método get para evitar errores al acceder a claves ausentes
# En análisis de datos, a veces leemos valores por clave que podrían no existir
valor_algo = datos.get("hola", "Clave no encontrada, intenta con otra")


#setdefault: garantiza que una clave exista con su valor por defecto
#En caso de que el método no encuentre la clave, la crea y le asigna
#el valor con el segundo parámetro ("desconocida")
resultado_setdefault = datos.setdefault("fuente de datos", "desconocida")


# Actualizar con otro diccionario (combinar datos)

datos_actualizados = {
    "límite_superior": 5.0,  # límite superior permitido para la medición
    "límite_inferior": 0.0,  # límite inferior permitido
}
datos.update(datos_actualizados)  # Actualiza/añade pares clave-valor


# En diccionarios, no existe append; usar update para fusionar dos mapeos
# Ejemplo alternativo: unir dos series simuladas
#dict3 = datos.update(datos_actualizados)  # no es válido para obtener un nuevo dict; update modifica en sitio
#print("Dict 3:", dict3)

#Método get

maximo = max(datos_actualizados.values())  # Devuelve el valor máximo de las medidas

# Copia de diccionario (útil para no mutar el original al realizar análisis)
dictCopy = datos_actualizados.copy()


# Propiedades útiles para inspección de datos


# Recorrer un diccionario valor a valor
#print("Presentar llaves una a una :")


peliculas = {
    "Inception": 12,
    "Avatar": 9,
    "Interstellar": 15,
    "Titanic": 7,
    "Avengers": 20
}

# Encontrar la película más votada
mas_popular = max(peliculas, key=peliculas.get)
