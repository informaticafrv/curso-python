cadena = str(input('escribe un a frase o una palabra: \n'))
caracter = str(input('escribe un caracter para comprobar que está: \n'))

if caracter in cadena:
    veces = cadena.count(caracter)
    print('el carácter está ', veces, ' veces en la cadena')
else:
    print('el carácter no está en la cadena')