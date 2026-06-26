cadena = str(input('introduce una cadena: \n'))
comprobacion = str(input('introduce que quieres que compruebe: \n'))

if comprobacion in cadena:
    print('la subcadena o caracter "', comprobacion,'" si está en la cadena original')
else:
    print('la subcadena o caracter "', comprobacion,'" no está en la cadena original')