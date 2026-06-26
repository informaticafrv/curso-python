salir = False
palabra = str(input('escribe una palabra o una frase: \n'))

while salir != True:
    caracter1 = str(input('escribe el carácter que quieres sustituir: \n'))
    caracter2 = str(input('escribe por que carácter quieres sustituirlo: \n'))
    if caracter1 in palabra:
        if caracter1 != caracter2:
            cadenaCambiada = palabra.replace(caracter1, caracter2)
            print('la cadena con los carácteres cambiados es: ', cadenaCambiada)
            salir = True
        else:
            print('los carácteres introducidos son el mismo')
    else:
        print('el caracter introducido no está en la cadena')