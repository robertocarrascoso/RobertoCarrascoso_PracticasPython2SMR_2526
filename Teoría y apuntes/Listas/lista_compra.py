lista_compra = []

elemento = ''

while elemento != 'quit':
    elemento = input('Introduce lo que quieres añadir a tu lista de la compra: ')
    lista_compra.append(elemento)
    lista_compra.remove('quit')

for i in lista_compra:
    if ('tomate' in i):
        print('No quedan tomates')
        lista_compra.remove(i)
print(lista_compra)