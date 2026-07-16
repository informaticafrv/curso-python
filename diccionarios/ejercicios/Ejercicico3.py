salir = False
frutas = {'manzana':1,'pera':2,'plantano':3}

while salir != True:
    nombre = str(input('escriba el nombre de la fruta: \n'))
    if nombre in frutas.keys():
        cantidad = int(input('escriba la cantidad de fruta que quiere comprar: \n'))
        precio = frutas[nombre] * cantidad
        print('el precio es: ', precio,'€')
        print('quiere volver a consultar otra fruta? \n')
        respuesta = str(input())
        if respuesta != 'si':
            print('vale, adiós')
            salir = True
    else:
        print('la fruta que ha solicitado no está disponible, por favor solicite otra')
        