#pide números por teclado hasta que se introduca un cero
#debe imprimir la suma y la media de todos los números introducidos
salir = False
nums = 0
contador = 0
while salir != True:
    introducido = int(input('escribe un número (para salir escribe 0): \n'))
    if introducido == 0:
        salir = True
    else:
        nums = nums + introducido
        contador = contador + 1
media = nums / contador
print('La suma de todos los números inroducidos es: ', nums ,'\nLa media es: ',media)