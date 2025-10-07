# Acceso a discoteca

edadUsr = int(input('Buenas noches. ¿Cuantos años tiene usted?: '))
vipUsr = bool(input('Dispone de pase VIP (si/no): '))
acompañado = bool(input('Viene acompañado de un adulto? (si/no): '))

if vipUsr == 'si':
    vipUsr = bool(True)
elif vipUsr == 'no':
    vipUsr = bool(False)
else:
    print('Intentalo de nuevo.')

if acompañado == 'si':
    acompañado = bool(True)
elif acompañado == 'no':
    acompañado = bool(False)
else:
    print('Intentalo de nuevo.')

if edadUsr >= 18:
    print('Puede entrar, disfrute de la noche.')
elif  vipUsr or acompañado:
    print('Puede entrar con este acceso especial, disfrute de la noche.')
else:
    print('Lo siento, pero no puede acceder.')