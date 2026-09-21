# OO_LightSwitch

class LightSwitch():
    def __init__(self):
        # Completa el atributo de estado

    def turnOn(self):
        # turn the switch on 
         # Completa

    def turnOff(self):
        # turn the switch off
         # Completa

    def show(self):  # added for testing
        # Completa
    
# Main code
oLightSwitch = LightSwitch()  # create a LightSwitch object

#  Calls to methods


'''
Se crea una clase LightSwitch que encapsula:
Estado: self.switchIsOn.
Comportamiento: turnOn, turnOff, show.
Crear una instancia (objeto) de la clase: oLightSwitch = LightSwitch().
El estado pertenece al objeto; no hay variables globales.
Ventajas visibles:
Múltiples interruptores: puedes crear varias instancias LightSwitch() sin interferencias entre ellas.
Organización: estado y comportamiento están agrupados.
Interfaz clara: se interactúa con métodos (turnOn, turnOff, show) y no con variables internas.

Recuerda que esta clase tiene una única variable de instancia llamada self.switchIsOn, 
pero su valor se recuerda y se accede fácilmente cuando se ejecutan diferentes métodos del mismo objeto.

1.1 Encapsulamiento y aislamiento del estado
Procedural: el estado se mantiene en una variable global. Cualquier parte del programa puede leer o modificar esa variable,
lo que facilita errores por cambios no intencionados y dificulta el razonamiento sobre el estado del sistema.
POO: el estado (en este caso, self.switchIsOn) está encapsulado dentro de una instancia de la clase. Solo los métodos 
del objeto pueden modificarlo (y, en teoría, se puede restringir su acceso desde fuera). Esto reduce efectos colaterales
 y facilita el razonamiento sobre el comportamiento del objeto.
1.2 Agrupación de datos y comportamiento
Procedural: los datos y las operaciones sobre ellos están dispersos (datos en variables y funciones separadas que actúan sobre esas variables).
POO: datos y comportamiento relevantes quedan unidos en una clase. Esto facilita:
Reutilización: puedes crear múltiples objetos LightSwitch independientes.
Extensibilidad: es fácil añadir más métodos (p. ej., toggle(), estado(), validaciones) sin desorganizar el código.
Mantenimiento: cambios en la lógica de encendido/apagado se implementan en un único lugar (los métodos de la clase).

'''