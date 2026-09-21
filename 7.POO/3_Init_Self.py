class FabricATelefonos():
    marca = "Apple" #Atributo

    def ElaborarHuawei(self): #Método de instancia, porque tiene la variable de instancia self
        self.marca = "Huawei"

telefono = FabricATelefonos()
marca1 = telefono.marca
print(marca1)
telefono.ElaborarHuawei()
print(telefono.marca)

class FabricATelefonos1():
    #método constuctor
    def __init__(self):
        print("Estoy ejecutando el método init, porque se ha creado un nuevo objeto")

Ntelefono = FabricATelefonos1()
Ntelefono2 = FabricATelefonos1()

class FabricATelefonos2():
    #método constuctor
    def __init__(self, marca, color, memoria, memoriaRam):
        self.marca = marca
        self.color = color 
        self.memoria = memoria
        self.memoriaRam = memoriaRam 

Telefono = FabricATelefonos2("Samsung", "gris", 8, 32)
print(f"Teléfono marca: {Telefono.marca}")
print(f"Teléfono de color: {Telefono.color}")

class PruebaLocal:
    def metodo_a(self):
        valor_local = 45 # Variable local
        return valor_local

    def metodo_b(self):
        try:
            return valor_local
        except NameError:
            return "valor_local no existe en el método_b"

Prueba = PruebaLocal()
print(Prueba.metodo_a())
print(Prueba.metodo_b())

class PruebaLocal2:
    def metodo_a(self):
        self.valor_local = 45 
        return self.valor_local

    def metodo_b(self):
        try:
            return self.valor_local*3
        except NameError:
            return "valor_local no existe en el método_b"

Prueba = PruebaLocal2()
print(Prueba.metodo_a())
print(Prueba.metodo_b())