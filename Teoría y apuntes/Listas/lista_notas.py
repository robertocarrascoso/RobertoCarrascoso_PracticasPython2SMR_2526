
lista_notas = []

while nota != '-1':
    nota = int(input('Introduce una nota (o introduce "-1" para salir).'))
    lista_notas.appedend(nota)

lista_notas.remove(-1)

suspensos = 0
aprobados = 0
notables = 0
sobresalientes = 0

print('Resultados: ')
for nota in lista_notas:
    if nota <0 and nota >10:
        print('Nota, ', nota, 'es incorrecta.')
    elif nota >= 0 and  nota < 5:
        print('Nota, ', nota, '-> Suspenso.')
        suspensos += 1
    elif nota <= 6:
        print('Nota, ', nota, '-> Aprobado.')
        aprobados += 1
    elif nota <= 8:
        print('Nota, ', nota, '-> Notable.')
        notables += 1
    else:
        print('Nota, ', nota, '-> Sobresaliente.')
        sobresalientes += 1

print('Resultados: ')
print('Suspensos:', suspensos)
print('Aprobados:', aprobados)
print('Notables:', notables,)
print('Sobresalientes:', sobresalientes)
