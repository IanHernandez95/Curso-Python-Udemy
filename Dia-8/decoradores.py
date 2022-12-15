# mi_funcion = mayuscula

# mi_funcion('python')
# def una_funcion(funcion):
#     return funcion
# una_funcion(mayuscula('probando'))

# def cambiar_letras(tipo):
    
#     def mayuscula(texto):
#         print(texto.upper())
    
#     def minuscula(texto):
#         print(texto.lower())

#     if tipo == 'may':
#         return mayuscula
#     elif tipo == 'min':
#         return minuscula

# operacion = cambiar_letras('may')
# operacion('palabra')

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('adios')
    return otra_funcion


def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())

mayuscula_decorada = decorar_saludo(mayuscula)

mayuscula_decorada('fede')