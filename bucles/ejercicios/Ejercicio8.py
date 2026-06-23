salir = False
terminar = False
inicio = 0
fin = 0
num = 0
suma = 0
numsF = 0
iguales = False
while salir != True:
    print('tienes que escribir dos números para tener un intervalo, uno donde empieza y otro donde acaba')
    inicio = int(input('escribe el número por el que empieza: \n'))
    fin = int(input('escribe el número por el que termina: \n'))

    if inicio > fin:
        print('el número por el que empieza el intervalo no puede ser mayor que por el que termina')
    else:
        salir = True

while terminar != True:
    print('ahora introduce todos los números que quieras, cuando termines introduce 0')
    num = int(input('escribe un número: \n'))
    if num == 0:
        terminar = True
    else:
        suma = suma + num
        if num > fin or num < inicio:
            numsF = numsF + 1
        if num == inicio or num == fin:
            iguales = True

if iguales == True:
    respuesta = 'sí'
else:
    respuesta = 'No'

print('la suma de los números introducidos: ', suma,'\n')
print('Números fuera de los límites: ', numsF, '\n')
print('se han introducido números iguales a los límites: ', respuesta)