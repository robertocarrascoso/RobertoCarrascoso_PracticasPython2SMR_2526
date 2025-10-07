usrCorrecto = 'siriguapa'
usrUsr = input('Introduzca su usuario: ')

pswdCorrecta = 'python123'
pswdUser = input('Introduce tu contraseña: ')

if pswdCorrecta == pswdUser and usrCorrecto == usrUsr:
    print('Acceso permitido.')
elif pswdCorrecta == pswdUser or usrCorrecto == usrUsr:
    print('El usuario o contraseña son incorrectos')
else:
    print('Acceso denegado.')
