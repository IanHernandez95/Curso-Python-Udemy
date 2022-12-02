

def chequear_3(lista):

    lista_3 = []
    
    for n in lista:
        if n in range(100,1000):
            lista_3.append(n)
        else:
            pass

    return lista_3

resultado = chequear_3([124,541,65])

print(resultado)