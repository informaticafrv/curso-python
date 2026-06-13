dia = int(input("escribe el dia: "))
mes = int(input("escribe el mes: "))
anio = int(input("escribe el año: "))
fechaValida = True

if anio > 2026:
    print("el año no puede ser superior al actual")
    fechaValida = False
if mes > 12 or mes < 1:
    print("el mes tiene que estar comprendido entre enero(1) y diciembre(12)")
    fechaValida = False
if dia < 1 or dia > 31:
    print("los días no pueden ser negativos ni superiores a 31")  
    fechaValida = False

if fechaValida == True:
    print("la fecha es: /",dia,"/",mes,"/",anio)