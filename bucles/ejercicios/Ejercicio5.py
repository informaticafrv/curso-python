salir = False

while salir != True:
    caracter = str(input('introduce un caracter y si quieres terminar introduce un espacio: \n'))
    if caracter == ' ':
        salir = True
    elif caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
        print('el caracter es una vocal')
    else:
        print('el caracter no es una vocal')