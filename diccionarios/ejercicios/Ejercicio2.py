cantidades = {}

frase = str(input('escribe una frase o palabra: \n'))

for caracter in frase:
    cantidades[caracter] = frase.count(caracter)

for clave,valor in cantidades.items():
    print(clave,' = ',valor)

