#básicamente son bloques trycatch como en java, se define lo que se quiere hacer y el tipo de error que se quiere controlar
try:
    num = int(input('intenta escribir un número \n'))
except ValueError:
    print('tiene que ser un número')

#ZeroDivisionError captura el error de dividir entre cero
num2 = input('dime un número para dividir')
try:
    print(10/num2)
except ValueError:
    print('tiene que ser un número')
except ZeroDivisionError:
    print('no se puede dividir por cero')
#también se puede usar un else por si ocurre cualquier otra excepción
else:
    print('se ha producido un error desconocido')
#y un finally para que pase lo que pase se ejecute este bloque
finally:
    print('siempre se ejecuta')



