import timeit


# def prueba_for(numero):
#     lista = []
#     for num in range(1,numero + 1):
#         lista.append(num)
#     return lista



# def prueba_while(numero):
#     lista = []
#     contador = 1
#     while contador <= numero:
#         lista.append(contador)
#         contador += 1
#     return lista

decla = '''
prueba_for(10)
'''
setu = '''
def prueba_for(numero):
    lista = []
    for num in range(1,numero + 1):
        lista.append(num)
    return lista
'''

duracion = timeit.timeit(decla,setu,number = 10000000)
print(duracion)

decla2 = '''
prueba_while(10)
'''
setu2 = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion2 = timeit.timeit(decla2,setu2,number = 10000000)
print(duracion2)
