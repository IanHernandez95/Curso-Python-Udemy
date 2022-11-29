mi_texto = 'Esta es una prueba'
# resultado = mi_texto[0] E
# resultado = mi_texto[9] n
# resultado = mi_texto[-4] u
# resultado = mi_texto.index('n') 9
# resultado = mi_texto.index('x') Error - No existe
# resultado = mi_texto.index('prueba') 12
# resultado = mi_texto.index('prueva') Error - Escritura
# resultado = mi_texto.index('Prueva') Error - Escritura
# resultado = mi_texto.index('a') 3 
# resultado = mi_texto.index('a',5) 10
# resultado = mi_texto.index('a',5,10) Error - No incluye el caracter 10
resultado = mi_texto.rindex('a')
print(resultado)