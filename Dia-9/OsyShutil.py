import os
import shutil
import send2trash

# archivo = open('curso.txt', 'w')
# archivo.write('Texto de Prueba')
# archivo.close()

# print(os.listdir())

# shutil.move('curso.txt', 'C:\\Users\\Ian\Documents\\Ejercicios Python\\Curso-Python-Udemy\\')

# send2trash.send2trash('curso.txt')

ruta = 'C:\\Users\\Ian\Documents\\Ejercicios Python\\Curso-Python-Udemy\\'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    print(f'Las subcarpetas son: ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('los Archivos son: ')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')