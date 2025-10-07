
print("SIMULADOR DE PUNTUACIONES DEPORTIVAS")

num_jugadores = int(input("¿Cuántos jugadores participan?: "))
nombres = []
medias = []

for i in range(num_jugadores):
    print("--- Jugador", i + 1, " ---")
    nombre = input("Nombre del jugador: ")
    nombres.append(nombre)
    
    print("Introduce las 3 puntuaciones de " + nombre + ": ")
    puntuacion1 = float(input("Ronda 1: "))
    puntuacion2 = float(input("Ronda 2: "))
    puntuacion3 = float(input("Ronda 3: "))
    
    media = (puntuacion1 + puntuacion2 + puntuacion3) / 3
    medias.append(media)


print("RESULTADOS INDIVIDUALES")

for i in range(num_jugadores):
    print(nombres[i] + ": Media = " + str(medias[i]))
    
    if medias[i] >= 8:
        print("El jugador " + nombres[i] + " es excelente")
    elif medias[i] >= 5:
        print("El jugador " + nombres[i] + " juega bien")
    else:
        print("El jugador " + nombres[i] + " necesita mejorar")


indice_ganador = 0
media_maxima = medias[0]

for i in range(1, num_jugadores):
    if medias[i] > media_maxima:
        media_maxima = medias[i]
        indice_ganador = i

print("GANADOR DEL TORNEO")
print("El jugador " + nombres[indice_ganador] + " es el ganador del torneo")
print("con una media de " + str(media_maxima))


aprobados = []
for i in range(num_jugadores):
    if medias[i] >= 5:
        aprobados.append(nombres[i])


print("JUGADORES APROBADOS (Media >= 5)")

if len(aprobados) > 0:
    print("Los siguientes jugadores han aprobado:")
    for nombre in aprobados:
        print(" - " + nombre)
else:
    print("No hay jugadores aprobados")


suma_total = 0
for media in medias:
    suma_total += media

media_general = suma_total / num_jugadores


print("ESTADÍSTICAS GENERALES")

print("Media general del grupo: " + str(media_general))
print("Total de jugadores: " + str(num_jugadores))
print("Jugadores aprobados: " + str(len(aprobados)))
