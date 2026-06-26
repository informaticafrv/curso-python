#los arrays no tienen indice, son literalmente un arraylist
numeros = [1,2,3,4,5,6]
for numero in numeros:
    print(numero)

#se pueden recorrer dos arrays a la vez en un mismo for
letras = ['a','b','c','d','e','f']
for numero,letra in zip(numeros,letras):
    print(numero,' ',letra)

#se pueden hacer comprobaciones igual que con los strings
numComprobacion = int(input('comprueba si un número está en la lista: \n'))
if numComprobacion in numeros:
    print('el número está en la lista')
else:
    print('el número no está en la lista')

#también con carácteres
caracComprobacion = str(input('comprueba que la letra está en la lista: \n'))
if caracComprobacion in letras:
    print('la letra está en la lista')
else:
    print('la letra no está en la lista')

#también se pueden sumar los arrays
numeros = numeros + [7,8,9,10,11,12,13,14]
for numero in numeros:
    print(numero)

#para coger un rango del array es igual que en el string
print(letras[2:4])

#para darle la vuelta también
print(numeros[::-1])

#para ver la lingitud de la lista
print('longitud de la lista de números: ',len(numeros))
print('logintud de la lista de letras: ',len(letras))

#valor máximo de una lista
print('el número más alto de la lista de números es: ',max(numeros))

#valor minimo
print('el número menor de la lista de números: ',min(numeros))

#sumar la lista de los números
print('la suma de la lista de los números: ',sum(numeros))

desordenada = [2,6,1,8,5,3,0,-1]
print('esta es la lista desordenada: ',desordenada)
desordenada = sorted(desordenada)
print('esta es la lista ordenada: ',desordenada)
desordenada = sorted(desordenada, reverse=True)
print('esta la lista ordenada al revés: ',desordenada)

#arrays bidimensionales
tabla = [[1,2,3],[4,5,6],[7,8,9]]
for fila in tabla:
    print('fila: ')
    for indice in fila:
        print(indice)

#para añadir un elemento al final del array
lista = [1,2,3]
lista.append(4)
print(lista)