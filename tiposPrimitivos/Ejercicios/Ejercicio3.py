#Dadas dos variables numéricas A y B, que el usuario debe teclear
#se pide realizar un algoritmo que intercambie los valores de ambas
# y muestre cuanto valen al final las dos variables
a = int(input("introduce el valor de la variable A: "))
b = int(input("introduce el valor de variable B: "))

aux = a
a = b
b = aux

print("la variable A vale:",a)
print("la variable B vale:",b)