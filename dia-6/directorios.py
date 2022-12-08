# import os
from pathlib import Path

# ruta = os.getcwd()
# ruta = os.chdir('C:\\Users\\Ian\\Documents\\Ejercicios Python\\Curso-Python-Udemy\\Alternativo - Dia 6')
# ruta = os.makedirs('C:\\Users\\Ian\\Documents\\Ejercicios Python\\Curso-Python-Udemy\\Alternativo - Dia 6\\otra')

# archivo = open('Alternativo.txt')

# print(archivo)


# ruta = 'C:\\Users\\Ian\\Documents\\Ejercicios Python\\Curso-Python-Udemy\\Dia-6'

# elemento = os.path.split(ruta)

# print(elemento)

# os.rmdir('C:\\Users\\Ian\\Documents\\Ejercicios Python\\Curso-Python-Udemy\\Alternativo - Dia 6\\otra')

# archivo2 = open('C:\\Users\\Ian\\Documents\\Ejercicios Python\\Curso-Python-Udemy\\Alternativo - Dia 6\\Alternativo.txt')

# print(archivo2.read())

carpeta = Path('C:/Users/Ian/Documents/Ejercicios Python/Curso-Python-Udemy/Alternativo - Dia 6')
archivo = carpeta / 'Alternativo.txt'

mi_archivo = open(archivo)

print(mi_archivo.read())