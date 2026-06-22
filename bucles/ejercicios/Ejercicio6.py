numsCorrectos = False
inicio = 0
fin = 0

print('te voy a decir los números pares que hay entre dos números, el primer número no puede ser mayor al segundo \n')

while numsCorrectos != True:
    inicio = int(input('introduce el número por que se va a empezar: \n'))
    fin = int(input('introduce el número en el que va a terminar: \n'))
    if inicio > fin:
        print('el número por el que se empieza no puede ser mayor que por el que se termina, vuelve a introducirlos, repite mostro')
    else:
        numsCorrectos = True

for i in range(inicio, fin):
    if i % 2 == 0:
        print(i,' ',end="")