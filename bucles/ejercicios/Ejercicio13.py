salir = False
horasB = False
diasB = False
horas = 0
dias = 0
sueldo = 0

print('Gestor de empleados')
print('-------------------')

while salir != True:
    horas = int(input('cuantas horas trabaja tu empleado?:\n'))
    dias = int(input('cuantos días a la semana?: \n'))
    sueldo = int(input('cuanto cobra por hora?: \n'))

    if horas <= 0 or horas > 8:
        print('las horas son incorrectas no pueden ser menores o iguales a 0 ni mayores de 8')
    else:
        horasB = True
    if dias <= 0 or dias > 6:
        print('los días no son correctos, no pueden ser menores o iguales a 0 ni mayores a 6')
    else:
        diasB = True
    
    if horasB == True and diasB == True:
        salir = True

horasMes = (horas * dias) * 4
sueldoMes = horasMes * sueldo
diasMes = dias * 4

print('datos del empleado\n')
print('----------------------------------------------')
print('horas que ha echado este mes: ',horasMes,'\n')
print('dias trabajados este mes: ',diasMes,'\n')
print('sueldo de este mes: ', sueldoMes)
print('----------------------------------------------')