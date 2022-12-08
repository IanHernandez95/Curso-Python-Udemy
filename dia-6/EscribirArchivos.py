# archivo = open('Prueba.txt', 'r') # Solo Lectura
# archivo = open('Prueba1.txt', 'w') # Se reemplaza el texto
archivo = open('Prueba1.txt', 'a') # Se agrega texto al final
# archivo.write('''Hola
# mundo
# aqui
# estoy''')
# archivo.writelines(['Hola','Mundo'])
# lista = ['Hola','Mundo']

# for p in lista:
#     archivo.write(p + '\n')

archivo.write('bienvenido')

archivo.close()