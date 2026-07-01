meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Dciembre']
salir = False
mes = 0
seleccionado = '';

while salir != True:
    mes = int(input('escribre un mes (1-12): \n'))
    if mes < 1:
        print('el mes no puede ser menor a 1')
    elif mes > 12:
        print('el mes no puede ser mayor a 12')
    else:
        seleccionado = meses.index(mes - 1)
        salir = True

if mes == 'Febrero':
    print('el mes ',mes,' tiene 28 días')
else:
    print('el mes ', mes,' tiene 31 días')


    