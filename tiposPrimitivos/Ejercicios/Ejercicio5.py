#pedir el nombre y los apellidos de una persona y mostrar las inicales.
nombre = str(input("escriba su nombre: "))
apellido1 = str(input("escriba su primer apellido: "))
apellido2 = str(input("escriba su segundo apellido: "))

iniciales = nombre[0].upper() + apellido1[0].upper() + apellido2[0].upper()

print("estas son tus iniciales:",iniciales)