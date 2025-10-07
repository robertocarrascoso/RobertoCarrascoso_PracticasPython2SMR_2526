nombre = input('¿Cómo te llamas?: ')
nacimiento = int(input('¿En qué año naciste?: '))

respuesta = input('¿Has pasado de curso? (si/no): ').lower()
haPasado = respuesta == 'si'

asignaturas = []

for i in range(1, 4):
    asignatura = input(f'Pon tu asignatura {i}: ')
    nota = float(input(f'Pon tu nota en {asignatura}: '))
    asignaturas.append((nota, asignatura))

edad = 2025 - nacimiento

mejorNota, mejorAsignatura = max(asignaturas)

print(f'\nTu nombre es {nombre} y tienes {edad} años.')
print(f'¿Pasaste de curso? {haPasado}')
print('Tus mejores notas fueron:')
for nota, asignatura in asignaturas:
    print(f' - {nota} en {asignatura}')

print(f'\nTu mejor nota fue un {mejorNota} en {mejorAsignatura}.')
