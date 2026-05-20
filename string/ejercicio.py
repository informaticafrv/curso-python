# para declarar simplemente se mete entre comillas y se reconoce como string
#concatenar con el + solo soporta string así que hay que hacer un casting
#concatenar con comas lo soporta todo y además añade espacios delaten y atrás
cadena1 = 'hola'
cadena2 = "hola 2"

#la triple comilla vale para escribir en varias líneas y que después se separe por \n
cadena3 = '''hola
que tal
como estás?'''
print(cadena1)
print(cadena2)
print(cadena3)

#también funciona la multiplicación por ejemplo
#si cogemos cadena uno y la multiplicamos se concatenará
#con ella misma las veces que le hayamos dicho
cadenaMulti = cadena1*10
print(cadenaMulti)

#el string también se comporta como un array de forma
#que podemos acceder a los carácteres concretos según su índice
print(cadena1[0])
print(cadena1[1])
print(cadena1[2])
print(cadena1[len(cadena1)-1])

