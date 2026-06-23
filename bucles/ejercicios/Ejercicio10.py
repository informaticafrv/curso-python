salir = False
tabla = 1

print('tablas de multiplicar del 1 al 5')

while salir != True:
    print('----------tabla del ',tabla,'---------')
    for i in range(1, 11):
        resultado = tabla * i
        print(tabla,' x ',i,' = ',resultado)
    print('--------------------------------')
    tabla = tabla + 1
    if tabla >= 5:
        salir = True
