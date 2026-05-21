#Un alumno desea saber cual será su calificación final en la materia
#dicha calificación se compone de los siguientes porcentajes
# * 55% del promedio de sus tres calificaciones parciales
# * 30% de la calificación del examen final
# * 15% de la calificación de un trabajo final
import math

parcial1 = float(input("escribe tu primera calificación: "))
parcial2 = float(input("escribe tu segunda calificación: "))
parcial3 = float(input("escribe tu tercera calificación: "))

parciales = (parcial1 + parcial2 + parcial3) / 3
print("la nota de tu examen es:",parciales)

examen = float(input("escriba la nota de su examen: "))

trabajo = float(input("escriba la nota de su trabajo: "))

nota = parciales *0.55 + 0.3 * examen + 0.15 * trabajo

print("tu nota final es:",nota)