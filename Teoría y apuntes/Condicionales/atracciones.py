# Programa parque de atracciones.

edadUsr = int(input('Bienvenido al Parque de Atracciones. ¿Que edad tienes?: '))
altraUsr = int(input('Cuantos cm (154) mides?: '))

if edadUsr >= 12 and altraUsr >= 140: 
    print('Puedes entrar, espero que disfrute de este maravilloso día.')
elif altraUsr > 160: 
    print('Puedes entrar acompañado de un adulto, buen día.')
else:
    print('No puedes pasar lo siento.')
