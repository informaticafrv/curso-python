letra = ''
salir = False
lista = []

while salir != True:
    letra = str(input('escribe una letra: \n'))
    if letra == 'salir':
        salir = True
    if len(letra) == 1:
        lista.append(letra)
        print('escribe "salir" para terminar el programa')
    else:
        print('tiene que ser una letra, vuelve a intentarlo \n')
    
invertida = lista[::-1]

print('lista de letras invertidas: \n')
for caracter in invertida:
    print(caracter)
