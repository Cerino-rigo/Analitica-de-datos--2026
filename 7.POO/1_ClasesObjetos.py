#Sintáxis de una clase
# class <Nombre de la clase>():

class FabricaTelefonos():
    pass

print(type(FabricaTelefonos))

celular = FabricaTelefonos() #Crear mi primer objeto, instanciación
print(type(celular))

celular2 = FabricaTelefonos() #Creamos un segundo objeto de la misma clase
print(type(celular2))

def FabricaTelefonos(): #No debemos generar funciones o variables con el mismo nombre
    #de una clase
    pass
print(type(FabricaTelefonos))