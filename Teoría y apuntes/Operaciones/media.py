

mediaPrimero = float(input('Cual fue tu media en Primero?: '))
mediaSegundo = float(input('Cual crees que será tu media en Segundo?: '))
notaCortegs = float(input('Que nota de corte necesitas para entrar al Grado Superior?: '))

mediaTotal = (mediaPrimero + mediaSegundo) / 2

if (mediaPrimero > notaCortegs):
    print('Eres un crack.')
elif (mediaTotal == notaCortegs):
    print('Bien, pero vas justo.')
else:
    falta = notaCortegs - mediaTotal
    print('Estudia, te queda', falta , 'puntos para poder acceder.')
