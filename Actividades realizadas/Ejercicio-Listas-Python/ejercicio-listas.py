estudiantes_notas = [['Cris', 8, 6, 9], ['Raul', 5, 7, 6]]
# nombre | nota_programación, nota_SER, nota_SOR

while True:
    nuevo_usuario = input("¿Quieres añadir un estudiante? si/no: ")
    if nuevo_usuario == "si":
        nombre_nuevo_usr = input("Nombre: ")
        nota_py = input("Nota de Python: ")
        nota_ser = input("Nota de SER: ")
        nota_sor = input("Nota de SOR: ")
        estudiantes_notas.append([nombre_nuevo_usr, nota_py, nota_ser, nota_sor])
        print("Se ha añadido a la lista el estudiante:", estudiantes_notas[-1])
    elif nuevo_usuario == "no":
        break
    else:
        print("Respuesta incorrecta, introduce si o no.")

for final_estudiante in estudiantes_notas:
    nombre = final_estudiante[0]
    nota1 = int(final_estudiante[1])
    nota2 = int(final_estudiante[2])
    nota3 = int(final_estudiante[3])
    
    suma = nota1 + nota2 + nota3
    promedio = round((suma / 3), 2) # El round es para redondear a 2 decimales
    
    print(nombre, "→ Notas:", nota1, ",", nota2, ",", nota3, "| Promedio:", promedio)

estud_registrados = len(estudiantes_notas)
print("Total de estudiantes registrados:", estud_registrados)