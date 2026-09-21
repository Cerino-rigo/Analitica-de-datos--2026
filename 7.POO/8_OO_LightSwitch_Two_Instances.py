# OO_LightSwitch

class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        # turn the switch on 
         self.switchIsOn = True

    def turnOff(self):
        # turn the switch off
         self.switchIsOn = False

    def show(self):  # added for testing
        print(self.switchIsOn)
    
# Main code


#  Test code


'''
El punto importante aquí es que cada objeto que creas a partir de una clase
mantiene su propia versión de los datos. En este caso, sala y cocina 
tienen cada uno su propia variable de instancia, self.switchIsOn. Cualquier cambio 
que hagas en los datos de un objeto no afectará los datos de otro objeto. 
Puedes llamar a cualquiera de los métodos en la clase con cualquiera de los objetos.

El código le dice a sala que se encienda y le dice a cocina que se apague.
Observa que el código en la clase no tiene variables globales. 
Cada objeto LightSwitch obtiene su propio conjunto de variables de instancia (solo una en este caso) definidas en la clase.

Si bien esto puede no parecer una gran mejora con respecto a tener dos variables globales simples 
que podrían usarse para hacer lo mismo, las implicaciones de esta técnica son enormes. 
Tendrás una mejor idea de esto conforme avancemos, tendrás una idea decómo crear y mantener 
una gran cantidad de instancias creadas a partir de una clase.

'''