def gen_perfumeria():
    num = 0
    while True:
        num += 1
        yield f'P-{num}'

def gen_farmacia():
    num = 0
    while True:
        num += 1
        yield f'F-{num}'

def gen_cosmetica():
    num = 0
    while True:
        num += 1
        yield f'C-{num}'

def decorar_turno(funcion):

    def otra_funcion():
        print('Su turno es :')
        print(next(funcion))
        print('Espere para ser Atendido')
    return otra_funcion



perfumeria = gen_perfumeria()
dec_perfumeria = decorar_turno(perfumeria)

farmacia = gen_farmacia()
dec_farmacia = decorar_turno(farmacia)

cosmetica = gen_cosmetica()
dec_cosmetica = decorar_turno(cosmetica)
