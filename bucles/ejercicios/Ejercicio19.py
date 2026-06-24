salir = False
atras = False

while salir != True:
    print('\n')
    print('*******************')
    print('bienvenido al menú')
    print('-----------------------------------------------')
    print('1. que el programa te salude')
    print('2. que el programa te diga el futuro')
    print('3. salir del programa')
    print('-----------------------------------------------')
    decision = int(input('escriba una de las opciones: \n'))
    
    print('respuesta: \n')
    match decision:
        case 1:
            print('hola maquinote')
        case 2:
            print('tu futúro es incierto fiera')
        case 3:
            print('adiós mastodonte')
            salir = True
        case _:
            print('solo tienes tres opciones xd')