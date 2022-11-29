texto = input('Ingrese un texto: ').lower()
letras = []

letras.append(input('Ingresa la primera letra: ').lower())
letras.append(input('Ingresa la segunda letra: ').lower())
letras.append(input('Ingresa la tercera letra: ').lower())

print('\n')
print('Cantidad de letras')
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f'Hemos encontrado la letras "{letras[0]}" repetida {cantidad_letras1} veces')
print(f'Hemos encontrado la letras "{letras[1]}" repetida {cantidad_letras2} veces')
print(f'Hemos encontrado la letras "{letras[2]}" repetida {cantidad_letras3} veces')

print('\n')

palabras = texto.split()
print(f'El largo del texto es {len(palabras)} palabras')

print('\n')
print(f'La primera letra del texto es "{texto[0]}" y la ultima letra del Texto es "{texto[-1]}"')

print('\n')
palabras.reverse()
t = ' '.join(palabras)
print(f'El texto escrito al reves seria: {t}')

print('\n')
python = 'python' in texto
dic = {
    True : 'Python esta en el texto',
    False : 'Python no esta en el texto'
}
print(dic[python])

