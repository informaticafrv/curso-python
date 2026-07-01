nombres = []
edades = []
salir = False

print('introduzca nombres y edades de sus alumnos: \n')
print('para terminar escriba como nombre "*"')

while salir != True:
    nombre = str(input('introduzca el nombre del alumno: \n'))
    edad = int(input('intorduzca su edad: \n'))
    
    if nombre == '*':
        salir = True

    if len(nombre) >= 3 and edad > 0:
        nombres.append(nombre)
        edades.append(edad)
    else:
        print('el nombre como mínimo tiene que tener 3 carácteres y la edad ser superior a 0')
    

print('mayores de edad')
print('---------------')

for nombre,edad in nombres,edades:
    if edad > 18:
        print('nombre: ',nombre,' edad: ',edad)
print('---------------')

print('menores de edad')
print('---------------')

for nombre,edad in nombres,edades:
    if edad < 18:
        print('nombre: ',nombre,' edad: ',edad)
print('---------------')