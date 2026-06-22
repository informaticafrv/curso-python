#crea una aplicación que permita adivinar un número
#genera un número aleatorio del 1 al 100 a continuación ve pidiendo números y va respondiendo
#si el número a adivinar es mayor o menor
#a demás de los intentos que te quedan (10 en total)
#el programa termina cuando se acierta o cuando se acaban los intentos
import random

salir = False
intentos = 10
numero = random.randint(1, 100)

while salir != True:
    if intentos == 10:
        print('tienes ', intentos,' intnetos para conseguirlo')
    intento = int(input('escribe un número a ver si lo adivino: \n'))
    if intento < numero:
        print('el número es mayor')
        intentos = intentos - 1
        print('te quedan ', intentos, ' intentos')
    elif intento > numero:
        print('el númeor es menor')
        intentos = intentos - 1
        print('te quedan ', intentos, ' intentos')
    else:
        print('has acertado!')
        salir = True
    if intentos == 0:
        print('has fallado y agotado todos los intentos')
        salir = True
    