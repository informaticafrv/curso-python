lista = []
salir = False

print('escriba números, si quiere parar introduzca un número negativo \n')
print('--------------------------------------------------------------')

while salir != True:
    num = int(input('escriba un nuevo número: \n'))
    if num < 0:
        salir = True
    else:
        lista.append(num)

for numero in lista:
    print(numero, ',')

