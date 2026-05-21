#hay que hacer un login que solo tiene un usuario y una contraseña
nombre = str(input("escriba su nombre de usuario: "))
contraseña = str(input("escriba su contraseña: "))

if nombre == "fran" and contraseña == "fran":
    print("has pasado el login máquina")
else:
    print("usuario o contraseña incorrectos")