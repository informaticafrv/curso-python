#esto es un diccionario básicamente un objeto literal como en js
tecnologias = {
    "Angular": "Frontend",
    "Laravel": "Backend",
    "React": "Frontend",
    "Spring Boot": "Backend"
}
#así se piden datos al usuario por teclado
nombre_usuario = input("Introduce tu nombre de desarrollador")
#mostramos su nombre
print(f"\n¡Perfecto, {nombre_usuario}! Vamos a analizar nuestro stack:\n")
#recorremos el diccionario con un for
for tecnologia, capa in tecnologias.items():
    #típicos if, esle, else if simples
    if capa == "Backend":
        print(f"⚙️ {tecnologia} es una herramienta potente para el backend")
    elif capa == "Frontend":
        print(f"🎨 {tecnologia} se encarga de la interfaz en el frontend")
    else:
        print(f"🤷 {tecnologia} no sé muy bien qué es")

print("\n--- Análisis completado con éxito ---")