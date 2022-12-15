# def suma():
#     n1 = int(input('Numero 1: '))
#     n2 = int(input('Numero 2: '))
#     print( n1 + n2 )
#     print('Gracias por sumar' + n1)

# # suma()

# try:
#     # Codigo a probar
#     suma()
# except TypeError:
#     # codigo a ejecutar si hay un error
#     print('Estas intentando concatenar tipos distintos')
# except ValueError:
#     print('Ese no es un numero')
# else:
#     # codigo a ejecutar si no hay un error
#     print('Hiciste todo bien')
# finally:
#     # codigo a ejecutar de todos modos
#     print('Eso fue todo')

def pedir_numero():

    while True:
        try:
            numero = int(input('Dame un numero: '))
        except:
            print('Ese no es un numero')
        else:
            print(f'Ingresaste el numero {numero}')
            break
    
    print('Gracias')

pedir_numero()