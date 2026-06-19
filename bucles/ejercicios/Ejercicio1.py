#crea una aplicación que pida un número y calcule su factorial
#(el factorial de un número es el producto de todos los enteros entre 1
#y el propio número y se representa por el número seguido de un signo de exclamación.
#por ejemplo 5! = 1x2x3x4x5 = 120
num = int(input('escriba el nombre para sacar el factorial: \n'))
factorial = 1
contador = 2
while contador <= num:
    factorial = factorial * contador
    contador = contador + 1
print('el resultado es: ', factorial)
 