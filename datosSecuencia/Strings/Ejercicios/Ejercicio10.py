cadena = str(input('escribe una cadena para comprobar si es un palíndromo: \n'))

invertida = cadena[::-1]

if cadena == invertida:
    print('la cadena',cadena,'si es un palíndromo')
else:
    print('la cadena', cadena,'no es un palíndromo')