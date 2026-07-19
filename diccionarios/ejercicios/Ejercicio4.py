salir = False
agenda = {}

while salir != True:
    print('BIENVENIDO AL MENÚ')
    print('------------------')
    print('1. Añadir')
    print('2. Modificar')
    print('3. Buscar')
    print('4. Borrar')
    print('5. Listar')
    print('6. Salir')
    print('------------------ \n')

    opcion = int(input())

    match opcion:
        case 1:
            nombre = str(input('Escriba el nombre de la persona que quiere añadir: \n'))
            numero = int(input('Ahora escriba su número: \n'))

            if nombre in agenda.keys():
                print('el nombre que ha seleccionado ya está registrado!')
            else:
                agenda[nombre] = numero
                print('número guardado! \n')

        case 2:
            nombre = str(input('escriba el nombre del cual quiere modificar el número: '))
            if nombre in agenda.keys():
                numero = int(input('escriba el nuevo número:  \n'))
                agenda[nombre] = numero
            else: 
                print('él nombre introducido no está en la agenda')
        
        case 3:
            nombre = str(input('escriba una cadena para buscar coincidencias: \n'))
            print('coincidencias: \n')
            for clave in agenda.keys():
                if clave.startswith(nombre):
                    print(clave)
        case 4:
            nombre = str(input('escribe el nombre de la persona que quieres borrar de la agenda: \n'))
            if nombre in agenda.keys():
                del agenda[nombre]
            else:
                print('esa persona no está registrada en la agenda')
        case 5:
            print('lsitado de la agenda: \n')
            for clave,valor in agenda.items():
                print(clave,' -> ',valor)
        case 6:
            print('adiós')
            salir = True

            
        