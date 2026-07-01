lista1 = []
lista2 = []
lista3 = []

print('Introduzca números para rellenar las dos listas: \n')

for i in range(0,5):
    lista1.append(int(input('escriba un número para la lista 1: \n')))
    lista2.append(int(input('escriba un número para la lista 2: \n')))

for num1,num2 in lista1,lista2:
    lista3.append(num1 + num2)

print('lista 1')
print('-------')
for num1 in lista1:
    print(num1)
print('-------')

print('lista 2')
print('-------')
for num2 in lista2:
    print(num2)
print('-------')

print('lista 3')
print('-------')
for num3 in lista3:
    print(num3)
print('-------')
