from random import shuffle
# Lista inicial
palitos = ['-','--','---','----']

# Mesclar los palitos
def mesclar(lista):
    shuffle(lista)
    return (lista)

# pedir al usuario 
def probar_suerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input('Elige un numero del 1 al 4: ')

    return int(intento)


# Comprobar el intento
def chequear_intento(lista,intento):
    if lista[intento - 1] == '-':
        print('Perdiste')
    else:
        print('Te has salvado')

    print(f'Te ha tocado el {lista[intento-1]}')

palos_mesclados = mesclar(palitos)
selecion = probar_suerte()
chequear_intento(palos_mesclados,selecion)

