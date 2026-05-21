#pide un número y que diga si es positivo negativo o 0
num = int(input("escribe un numero: "))

if num < 0:
    print("el numero",num,"es negativo")
elif num == 0:
    print("el numero",num,"es igual a cero")
else:
    print("el numero",num,"es un número positivo")