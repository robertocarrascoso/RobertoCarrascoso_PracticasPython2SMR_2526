import random


eleccion = input(
        'Ejercicio: \n'
        ' a. Bienvenida \n'
        ' b. Mensaje de ánimo \n'
        ' c. Despedida \n'
        ' d. Número aleatorio \n'
        ' e. Tirar dados \n'
        'Por favor selecciona una de las opciones (a | b | c | d | e): ')

if eleccion == 'a':
    print('Bienvenido a casa señor.')
elif eleccion == 'b':
    print('Hoy hace un día estupendo, mucho ánimo y aprovechalo.')
elif eleccion == 'c':
    print('Hasta luego.')
    
elif eleccion == 'd':
    numeroRandom = random.randint(1, 100)
    print('Este es tu número aleatorio:', numeroRandom)
elif eleccion == 'e':
    dado = random.randint(1, 6)
    print('El dado ha caído en el:', dado, '.')
else:
    print('Error, escriba una de estas letras (a | b | c | d | e): ')