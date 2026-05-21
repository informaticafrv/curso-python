#primero el while por algún motivo
entrado = False
contador = 0
contraseña = ""
while contraseña != "contraseña":
    if entrado != True:
        entrado = True
    else:
        print("contraseña incorrecta")
        contador+=1
    contraseña = str(input("escribe la contraseña: "))
    if contador >= 3:
        print("cagaste")
        break
print("has salido del bucle campeón")
