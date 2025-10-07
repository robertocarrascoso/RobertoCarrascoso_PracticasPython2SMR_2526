
num_jugadores = int(input("Introduce el número de jugadores: "))


nombres = []
puntuaciones = []
medias = []

for i in range(num_jugadores):
    print(f"Jugador {i+1}:")
    nombre = input("  Nombre: ")
    nombres.append(nombre)

    rondas = []
    for r in range(1, 4):
        puntuacion = float(input(f"Puntuación ronda {r}: "))
        rondas.append(puntuacion)
    puntuaciones.append(rondas)

print("Resultados individuales:")
for i in range(num_jugadores):
    media = sum(puntuaciones[i]) / len(puntuaciones[i])
    medias.append(media)
    print(f"- {nombres[i]} → Media: {media:.2f}")

    if media >= 8:
        print(f"El jugador {nombres[i]} es excelente")
    elif media >= 5:
        print(f"El jugador {nombres[i]} juega bien")
    else:
        print(f"El jugador {nombres[i]} necesita mejorar")

mayor_media = max(medias)
indice_ganador = medias.index(mayor_media)
ganador = nombres[indice_ganador]
print(f"El jugador {ganador} es el ganador del torneo con una media de {mayor_media:.2f}")

aprobados = [nombres[i] for i in range(num_jugadores) if medias[i] >= 5]
print("Jugadores aprobados (media ≥ 5): " + ", ".join(aprobados))

media_general = sum(medias) / num_jugadores
print(f"Media general del grupo: {media_general:.2f}")