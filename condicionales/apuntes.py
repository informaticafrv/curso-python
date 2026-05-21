#los ifs son sencillos en vez de haber llaves simplemente entra dentro de la condición lo que esté indexado debajo
#por ejemplo:
interruptor = False
accion = str(input("quieres encender la luz?"))
accion.lower()
#además no se usan paréntesis y tiene que terminar en : 
if accion == "si":
    if interruptor == True:
        print("la luz ya estaba encendida")
    else:
        interruptor = True
else:
    if interruptor == False:
        print("la luz ya estaba apagada")
    else:
        interruptor = False

if interruptor == True:
    print("la luz está encendida")
else:
    print("la luz está apagada")