#boolean
salir = True
entrar = False
if type(salir) == bool:
    print("salir es true y es un bool")
if type(entrar) == bool:
    print("entrar es false y también es bool")
#int
num = 5
if type(num) == int:
    print("num es un número entero:",num)
#float
numD = 5.2
if type(numD) == float:
    print("numD es un número decimal y su tipo es float:",numD)
print("escribe tu edad:")
#como pedir datos por consola
edad = int(input("edad:"))
#no hace falta ponerle espacios cuando se concatena con comas como en java
if edad > 18:
    print("eres mayor de edad")
else:
    print("no eres mayor de edad")
#con el % se formatea la salida de un string
producto = "cesta"
cantidad = 23
precio = 13.456
print("producto %s, cantidad: %s ,precio: %.2f"%(producto, cantidad, precio))
