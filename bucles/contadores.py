# un contador normalito bucle de cinco iteraciones pide números cuenta los pares y muestra el contador
contador = 0
for i in range(0,5):
    num = int(input('dime un número: \n'))
    if num % 2 == 0:
        contador = contador + 1
print('has introducido',contador,'números pares')