# DimmerSwitch class

class DimmerSwitch():
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0
        
    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    # Extra method for debugging
    def showState(self):
        



# Main code


# Turn switch on, and raise the level 5 times


# Lower the level 2 times, and turn switch off


# Turn switch on, and raise the level 3 times


'''
En este método __init__() tenemos dos variables de instancia: la familiar self.switchIsOn 
y una nueva, self.brightness, que recuerda el nivel de brillo. Asignamos valores iniciales
a ambas variables de instancia. Todos los demás métodos pueden acceder al valor 
actual de cada una de ellas. Además de turnOn() y turnOff(), incluimos dos nuevos métodos
para esta clase: raiseLevel() y lowerLevel(), que hacen exactamente lo que sus nombres implican. 
El método show() se utiliza durante el desarrollo y la depuración y simplemente 
imprime los valores actuales de las variables de instancia.
'''

'''
El código principal crea el objeto oDimmer y luego realiza llamadas a los diversos métodos. 
Cada vez que llamamos al método show(), se imprimen el estado de encendido/apagado y el nivel de brillo. 
Lo fundamental para recordar aquí es que oDimmer representa un objeto. Permite el acceso 
a todos los métodos de la clase desde la que se instanció (la clase DimmerSwitch), 
y tiene un conjunto de todas las variables de instancia definidas en la clase (self.switchIsOn y self.brightness). 
De nuevo, las variables de instancia mantienen sus valores entre las llamadas a los métodos de un objeto, 
por lo que la variable de instancia self.brightness se incrementa en 1 por cada llamada a oDimmer.raiseLevel().

'''
#Crear 3 instancias de la clase DimmerSwitch y mostrar que cada una mantiene su propio estado.
# Main code
#objeto1 esté encendida al 100%;
#objeto2 esté apagada;
#objeto3 esté encendida al 50;



#Puedes inspeccionar todas las variables de instancia en un objeto 
#llamando a la función incorporada vars() en cualquier objeto.

