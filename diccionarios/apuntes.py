#los diccionarios son listas con claves asociadas a un valor, básicamente un hashmap
diccionario = {'one':1, 'two':2, 'three':3}

#para acceder a un valor concreto simplemente se accede al índice nombrando la clave
print(diccionario['one'])

#también se puede declarar vacío e ir añadiendo valores, no tienen orden establecido
nombres ={}
nombres['primero'] = 'Juan'
nombres['segundo'] = 'José'

#también se puede usar len para saber el número de elementos del diccinario
len(nombres)

#se pueden comprobar claves con in
if 'primero' in nombres:
    print('hay nombres en el diccionario')

#y también podemos copiar un diccionario en otro con la función copy
copia = diccionario.copy()

#con la función update se pueden añadir elementos o incluso otro diccionario entero
diccionario.update(copia)

#para acceder a los valores lo mejor es usar el método get
diccionario.get('primero')

#para recorrer las claves
for clave in diccionario.keys():
    print(clave)

#para recorrer los valores
for valor in diccionario.value():
    print(valor)

#para recorrer los dos
for clave,valor in diccionario.items():
    print(clave,' = ',valor)
