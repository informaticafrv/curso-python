numeros = {}
limite = int(input('escribe hasta donde quieres que llegue la lista: \n'))

for i in range(0,limite):
    cuadrado = i * i
    numeros[i] = cuadrado

print('esta es la lista')
print(numeros)