# Procedural light switch

def turnOn():
    global switchIsOn
    # turn the light on 
    switchIsOn = True

def turnOff():
    global switchIsOn
    # turn the light off
    switchIsOn = False
    
# Main code
switchIsOn = False     # a global Boolean variable

# Test code


#
''' 
Usa una variable global switchIsOn para representar el estado.
Funciones turnOn y turnOff modifican ese estado global.
El flujo es directo y funciona para ejemplos simples, pero presenta varias desventajas:
Dependencia de una variable global, lo que hace menos predecible y más difícil de rastrear en programas grandes.
Dificultad para crear múltiples interruptores independientes (solo una variable global, no varios objetos).
Pruebas unitarias más complicadas: hay que restablecer el estado global entre pruebas.
'''