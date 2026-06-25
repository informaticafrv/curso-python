primo = True
num = int(input('introduce un  número para comprobar si es primo o no: \n'))

for i in range(2, num):
    if num % i == 0:
        primo = False

if primo:
    print('es primo')
else:
    print('no es primo')