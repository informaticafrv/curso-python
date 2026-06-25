cadena = str(input('escribe una palabra o una frase: \n'))
comprobacion = str(input('escribe un caracter o palabra para comprobar si está o no: \n'))

if comprobacion in cadena:
    print(comprobacion,' si está en la cadena')
else:
    print(comprobacion,' no está en la cadena')