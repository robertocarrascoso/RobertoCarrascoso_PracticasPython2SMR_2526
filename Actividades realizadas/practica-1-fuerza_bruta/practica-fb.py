import random

usuarios = []
while True:
    nombre = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    usuarios.append([nombre, contraseña])
    decision = input("¿Quieres añadir un nuevo usuario? (si/no): ")
    if decision != "si":
        break

contras_comunes = ["1234", "password", "Administrador", "user@123", "abc123", "hola", "admin"]

vulnerados = []
resistentes = []

while True:
    ataque = input("¿Quieres hacer un ataque aleatorio? (si/no): ")
    if ataque != "si":
        break

    usuario = random.choice(usuarios)
    nombre_while = usuario[0]
    contraseña_while = usuario[1]
    vulnerable = False

    for contraseña in contras_comunes:
        if contraseña_while == contraseña:
            print("El usuario", nombre_while , "fue vulnerado. Contraseña débil.")
            vulnerable = True
            break
    if vulnerable:
        vulnerados.append(nombre_while)
    else:
        print("El usuario", nombre_while , "resistió el ataque.")
        resistentes.append(nombre_while)

print("Usuarios vulnerados:", vulnerados)
print("Usuarios NO vulnerados:", resistentes)
