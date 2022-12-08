import os
from pathlib import Path
import time

# Variables Globales
loop = True
base = Path(Path.home(),'Recetas')


# funciones
def mostrar_categoria(ruta):
    categorias = os.listdir(ruta)
    return categorias

def contar_recetas(ruta):
    cant_recetas = 0
    for path in Path(ruta).glob('**/*.txt'):
        if path.is_file():
            cant_recetas += 1
    return cant_recetas

def elegir_categoria(categorias):
    while True:
        print(f'Hay las Siguentes Categorias: { " - ".join(categorias) }')
        opcion = input('Que Categoria quiere Elegir: ').capitalize()
        if opcion not in categorias:
            print('Opcion no Valida - Ingrese una de las Disponibles')
        else:
            return Path(base, opcion)
            

def leer_receta(categoria):
    while True:
        recetas = os.listdir(categoria)
        if len(recetas) < 1:
            print('Esta categoria no tiene recetas')
            return
        else:
            print(f'Hay las Siguentes Categorias: { " - ".join(recetas) }')
            eleccion = input('Que receta quiere leer: ')
            for r in recetas:
                if eleccion in r.lower():
                    ruta = Path(categoria,r) 
                    print(Path.read_text(ruta))                    
                    return 
        print('Opcion no Valida - Ingrese una de las Disponibles')

def crear_receta(categoria):
    nombre = input('Ingrese el nombre de la Receta: ').capitalize()
    n_receta = Path(categoria, f'{nombre}.txt')
    receta_nueva = open(n_receta,'w')
    texto = input('Ingrese la Receta: ')
    receta_nueva.write(texto)

def crear_categoria():
    nombre_cat = input('Ingrese la Categoria a Crear: ').capitalize()
    directorio = Path(base,nombre_cat)
    os.makedirs(directorio)

def eliminar_receta(categoria):
    while True:
        recetas = os.listdir(categoria)
        print(f'Hay las Siguentes Categorias: { " - ".join(recetas) }')
        eleccion = input('Que receta quiere eliminar: ')
        for r in recetas:
            if eleccion in r.lower():
                ruta = Path(categoria,r)
                os.remove(ruta)
                print(f'La receta {r} fue eliminada')
                return 
        print('Opcion no Valida - Ingrese una de las Disponibles')

def eliminar_categoria(categorias):
    while True:
        print(f'Hay las Siguentes Categorias: { " - ".join(categorias) }')
        opcion = input('Que Categoria quiere Eliminar: ').capitalize()
        if opcion not in categorias:
            print('Opcion no Valida - Ingrese una de las Disponibles')
        else:
            ruta = Path(base, opcion)
            recetas = os.listdir(ruta)
            for r in recetas:
                rem = Path(ruta,r)
                os.remove(rem)
            os.rmdir(ruta)
            print(f'La categoria {opcion} y sus archivos fueron eliminados exitosamente')
            return


# Loop Principal
print("**************************************************") 
print("*                                                *")
print("*                   Bienvenido                   *")
print("*                                                *")
print(f"*    La ruta de acceso es {base}   *")
print("*                                                *")
print(f"* La cantidad de recetas en este directorio es {contar_recetas(base)} *")
print("*                                                *")
print("**************************************************")
while loop:
    time.sleep(1)
    os.system('cls')
    print("**************************************************")
    print("*                                                *")
    print("*                    Menu                        *")
    print("*             Opcion 1: Leer Receta              *")
    print("*         Opcion 2: Crear Receta Nueva           *")
    print("*         Opcion 3: Crear una Categoria          *")
    print("*         Opcion 4: Eliminar una Receta          *")
    print("*       Opcion 5: Eliminar una Categoria         *")
    print("*         Opcion 6: Salir del Programa           *")
    print("*                                                *")
    print("**************************************************")
    menu = int(input('Ingrese el numero de su opcion: '))
    if menu == 1:
        os.system('cls')
        mi_categoria = mostrar_categoria(base)
        os.system('cls')
        cat_elegida = elegir_categoria(mi_categoria)
        os.system('cls')
        leer_receta(cat_elegida)
    elif menu == 2:
        os.system('cls')
        mi_categoria = mostrar_categoria(base)
        os.system('cls')
        cat_elegida = elegir_categoria(mi_categoria)
        os.system('cls')
        crear_receta(cat_elegida)
        print('Receta Creada con exito')
    elif menu == 3:
        os.system('cls')
        crear_categoria()
        print('Categoria creada con exito')
    elif menu == 4:
        os.system('cls')
        mi_categoria = mostrar_categoria(base)
        os.system('cls')
        cat_elegida = elegir_categoria(mi_categoria)
        os.system('cls')
        eliminar_receta(cat_elegida)
    elif menu == 5:
        os.system('cls')
        mi_categoria = mostrar_categoria(base)
        os.system('cls')
        eliminar_categoria(mi_categoria)
    elif menu == 6:
        print("**************************************************") 
        print("*                                                *")
        print("*            Gracias - Vuelva Pronto             *")
        print("*                                                *")
        print("**************************************************") 
        time.sleep(2)
        loop = False
    else:
        print('Opcion no Validad - Intentelo Nuevamente')

