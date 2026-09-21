class FabricATelefonos():

    #Atributos de mi objeto
    marca = "Apple"
    color = "Negro"
    memoria = 128
    memoriaRam = 8

    #Métodos de una clase
    def llamar(self, mensaje):
        return mensaje

    def tomarFotos(self):
        print("Sonríe, te estamos tomando una foto")


telefono = FabricATelefonos() #Crear primer objeto, o instanciarlo
print(telefono)

#Acceder a atributos de mi objeto
telefono.marca #Asignamos el atributo marca al objeto telefono
print("Accediendo a un atributo de mi objeto teléfono: ")
print(telefono.marca)
print(telefono.memoria)

#Acceder a los métodos desde el objeto
llamada = telefono.llamar("Hola, ¿con quién hablo?")
print(llamada)
telefono.tomarFotos()