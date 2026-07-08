salirMenu = False
lista = []
while salirMenu != True:
    print('bienvenido al menú')
    print('------------------')
    print('1. Añadir un número')
    print('2. Añadir un número en un posición concreta')
    print('3. Consular lingitud de la lista')
    print('4. Eliminar el último número')
    print('5. Eliminar un número de una posición concreta')
    print('6. Contar cuantas veces aparece un número')
    print('7. Posición de un número')
    print('8. Mostrar números')
    print('9. Salir')

    decision = int(input('elije colegui: \n'))
    match decision:
        case 1:
            anadir = int(input('escribe el número que quieres añandir: \n'))
            lista.append(anadir)
        case 2:
            indice = int(input('escribe el indice en el que quieres añadir: \n'))
            numIndice = int(input('escribe el número a añadir: \n'))
            lista[indice] = numIndice
        case 3:
            print('la longitud de la lista es: ', len(lista))
        case 4:
            lista.pop()
            print('elemento eliminado!')
        case 5:
            posicion = int(input('escribe la posición que quieres eliminar: \n'))
            lista.pop(posicion)
            print('elemento eliminado')
        case 6:
            contador = 0
            num = int(input('escribe que número quieres contar: \n'))
            for num in lista:
                if num == lista:
                    contador = contador + 1
            print('el número de veces que aparece es: ',contador)
        case 7:
            num = int(input('escribe el nombre del que quieres saber el indice: \n'))
            indice = lista.index(num)
            print('el indice de tu numero es: ', indice)
        case 8:
            print('esta es la lista de números: \n')
            print('----------------------------')
            for num in lista:
                print(num)
        case 9:
            print('nos vemos!')
            salirMenu = True