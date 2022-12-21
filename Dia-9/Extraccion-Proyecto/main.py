import os
import re
import datetime
import time
from pathlib import Path
import math

inicio = time.time()

ruta = 'C:\\Users\\Ian\\Documents\\Ejercicios Python\\Curso-Python-Udemy\\Dia-9\\Extraccion-Proyecto\\Mi_Gran_Directorio'
mi_patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
nros_encontrados = []
arc_encontrados = []

def buscar_numero(archivo, patron):
    este_archivo = open(archivo,'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''

def crear_listas():
    for carpeta, subcarpetas, archivos in os.walk(ruta):
        for a in archivos:
            resultado = buscar_numero(Path(carpeta,a),mi_patron)
            if resultado != '':
                nros_encontrados.append(resultado.group())
                arc_encontrados.append(a.title())


def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de Busqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')
    for a in arc_encontrados:
        print(f'{a}\t\t{nros_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Número encontrados: {len(nros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duracion de la Busqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)


crear_listas()
mostrar_todo()