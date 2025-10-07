
peliculas_a_ver = []

while True:
    addFilm = input('¿Qué película quieres ver? (Pulsa q para salir): ')
    
    if addFilm.lower() == 'q':
        break

    if addFilm == 'Titanic':
        print('La película Titanic ya la has visto muchas veces, elige otra.')
        continue
    
    peliculas_a_ver.append(addFilm)

def mostrar_lista(peliculas):
    if not peliculas:
        return "No has añadido ninguna película."
    return ', '.join(peliculas)

print("Películas a ver:", mostrar_lista(peliculas_a_ver))
