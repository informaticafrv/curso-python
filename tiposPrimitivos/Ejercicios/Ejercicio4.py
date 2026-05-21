#un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos
# el tiempo de viaje hasta llegar a otra ciudad B es de T segundos
#escribir un algoritmp que determine la hora de llegada a la ciudad

hora = int(input("introduce la hora: "))
minutos = int(input("introduce los minutos: "))
segundos = int(input("introduce los segundos: "))

origen = str(input("introduce el nombre de la ciudad en la que estás: "))
destino = str(input("introduce el nombre de la ciudad a la que quieres ir: "))

recorrido = int(input("introduce el tiempo que se tarde en llegar allí: "))

horaS = hora * 3600
minutosS = minutos * 60
segundosS =segundos + horaS + minutosS

segundosS += recorrido

horaLLegada = segundosS // 3600
minllegada = (segundosS % 3600) // 60
segundosllegada = (segundosS % 3600) % 60

print("saliendo de",origen,"hasta",destino," a las",hora,":",minutos,":",segundos,"llegarías allí a las",horaLLegada,":",minllegada,":",segundosllegada,".")
