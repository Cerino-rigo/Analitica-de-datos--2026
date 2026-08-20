ruta = "ventas_2026.txt"
  #Método with/as cierra automáticamente el archivo, 
   
with open(ruta, mode="r", encoding="utf-8") as fichero:
  
    datos = fichero.readlines()

    #print(datos)

    #¿Cómo podemos separar "Laptop" y "15000"?
    #print(datos[0])

   
if fichero.closed: 
    print("El archivo se ha cerrado correctamente" )
else: 
    print("El archivo permanece abierto")