# def devolver_distintos(a,b,c):
#     lista = [a,b,c]
#     suma = a + b + c 
#     if suma > 15:
#         return max(lista)
#     elif suma < 10:
#         return min(lista)
#     else:
#         lista.sort()
#         return lista[1]

# print(devolver_distintos(10,1,3))

# def ordenar_letras(palabra):
    # letras = list(palabra.lower())
    # l_no_repetido = []
    # for l in letras:
    #     if l not in l_no_repetido:
    #         l_no_repetido.append(l)
    #     else:
    #         pass
    # l_no_repetido.sort()
    # return l_no_repetido
#     mi_set = set()
#     for l in palabra:
#         mi_set.add(l)
#     mi_lista = list(mi_set)
#     mi_lista.sort()
#     return mi_lista

# print(ordenar_letras('entretenido'))

# def comprobar_0(*args):
#     contador = 0
#     for n in args:

#         if contador + 1 == len(args):
#             return False

#         elif args[contador] == 0 and args[contador+1] == 0:
#             return True
#         else:
#             contador += 1

#     return False

# print(comprobar_0(0,1,2,6,0,1,3,0,5,1,23,2,0))


def contar_primos(num):
    
    primos = [2]
    iteracion = 3

    if num < 2:
        return 0

    while iteracion <= num:
        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break            
        else:
            primos.append(iteracion)
            iteracion += 2

    print(primos)
    return len(primos)

print(contar_primos(50))




contar_primos(8)
