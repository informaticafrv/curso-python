num = 0
salir = False

while salir != True:
    num = int(input('escribe un número para mostrar su tabla de multiplicar (que no sea menor a 0): \n'))
    if num >= 0:
        salir = True

print('tabla del: ',num)
print('----------------')
for i in range(0, 11):
    resultado = num * i
    print(i,' x ', num,' = ', resultado)
