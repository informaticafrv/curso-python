#para hacer funciones se usa def nombreFuncion(n):
def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

num1 = int(input('escribe un número: \n'))
num2 = int(input('escribe otro para sumarlos"\n'))

resultado = sumar(num1, num2)

print('el resultado es: ',resultado)

#factorial con recursiva
def factorialR (num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorialR(num-1)

print(factorialR(5))
