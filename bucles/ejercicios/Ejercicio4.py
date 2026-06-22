#se pide cuantos números se van a introducir
# y se van contado cuantos números son menores que 0 mayores que 0 e iguales a 0

cantidad = int(input('cuantos números quieres que se pidan? \n'))

mayores = 0
menores = 0
iguales = 0

for i in range(0, cantidad):
    num = int(input('introduce un número: \n'))
    if num > 0:
        mayores = mayores + 1
    elif num == 0:
        iguales = iguales + 1
    else:
        menores = menores + 1

print('números mayores a 0: ',mayores,'\n números menores a 0:', menores,'\n números iguales a 0:', iguales)