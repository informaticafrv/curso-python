notas = []
contador = 1
media = 0

print('escribe tus cinco notas')
for i in range(0,5):
    nota = int(input('escribe la nota: \n'))
    if nota > 0 and nota < 11:
        notas.append(nota)

print('INFORMACIÓN DE TUS NOTAS')
print('------------------------')
print('notas: \n')
for calificacion in notas:
    print('nota ',contador,': ', calificacion)
    contador = contador + 1

print('-----------------------')
print('nota media: \n')
media = sum(notas) / len(notas)
print(media)
print('----------------------')
print('nota más alta: \n', max(notas))
print('nota más baja: \n', min(notas))
print('----------------------')