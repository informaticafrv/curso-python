cadena = str(input('escribe una palabra o una frase: \n'))
#así se recorre una cadena como si fuera un foreach
for letra in cadena:
    print(letra)

#con el in se puede saber directamente si una cadena está en el string
if 'a' in cadena:
    print('la letra a está en el string')
else:
    print('la letra a no está en el string')

#recoge de la posición 0 a la 2
print(cadena[0:2])
#recoge de la posición 2 a la última
print(cadena[2:])
#recoge la cadena entera, pero invertida
print(cadena[::-1])

#upperCase
mayus = cadena.upper()
print(mayus)

#lowerCase
minus = cadena.lower()
print(minus)

#pone la primera en mayúscula
primeraMayus = cadena.capitalize()
print(primeraMayus)

#invierte mayúsculas y minúsculas
invertMayMin = cadena.swapcase()
print(invertMayMin)

#pone la primera letra de cada palabra en mayúscula
titulo = cadena.title()
print(titulo)

#contar cadenas dentro de una cadena (se pueden usar carácteres, cadenas enteras para contar o nada y que cuente toda la logitud)
contar = cadena.count('')
contarA = cadena.count('a')
contarHola = cadena.count('hola')
contarDesdePosicion = cadena.count('a',16)
contarDesdeRango = cadena.count('a',10,16)
print('número de carácteres: ',contar,'\n número de carácter a: ', contarA, '\n número de veces que aparece la palabra hola: ',contarHola)

#posición de primera concurrecia, si no la encuentra devuelve -1
primeraConcurrencia = cadena.find('tardes')
print('la primera concurrencia está en la posición: ', primeraConcurrencia)

#comprobar con que empieza
if cadena.startswith('hola'):
    print('la cadena empieza con hola')
else:
    print('la cadena no empieza con hola')

#comprobar con que termina
if cadena.endswith('noches'):
    print('la cadena termina con la palabra noches')
else:
    print('la cadena no termina con la plabra noches')

#el típico replacce
remplazar = cadena.replace('a', 'x')
print('cadena remplazando las a por x: ',remplazar)

#quitar espacios de adelante y atrás como un .trim
limpieza = cadena.strip()
print('cadena sin espacios al comienzo y al final: ',limpieza)
#también se le pueden quitar otros carácteres que no sean espacios
limpieza2 = cadena.strip('/')
print('cadena sin / al comienzo o al final: ', limpieza2)

#spliteo de toda la vida
cadeanSpliteada = cadena.split(' ')
for palabra in cadeanSpliteada:
    print(palabra)

#splitear con saltos de linea
texto = 'linea 1\nlinea 2\nlinea 3'
textoSplit = texto.splitlines()
for linea in textoSplit:
    print(linea)

