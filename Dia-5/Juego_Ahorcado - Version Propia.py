from random import *

lista_palabras = ['mariposa','auto','casa','colegio','computador','gato','perro','primavera','caja','verano','libro',
    'esternocleidomastoideo','desoxirribonucleico','dinosaurio','helicoptero','panadero','chef','bailarina',"guerra",
    "paz","camiseta","fuego","tierra","planeta","sol","luna","jupiter","urano","pluton","libreta","marte","mercurio",
    "venus","galaxia","universo","guitarra","musica","piano","cenicero","tambor","arte","artesania","violin",
    "correr","saltar","saturno","estrella"]


def mostrar_guiones():
    palabra_azar = choice(lista_palabras)
    guiones = '-'*len(palabra_azar)
    return palabra_azar, guiones

palabra,guion = mostrar_guiones()

def ahorcado(palabras, guiones):
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    vidas = ['<3','<3','<3','<3','<3','<3']
    can_vidas = 6
    adivinar = list(palabras)
    g_adivinar = list(guiones)
    p_adivinada = ''
    intentos = []
    nombre = input('Ingresa tu nombre: ')
    print(f'Hola {nombre} Este es el juego del ahorcado')
    print(f'Tu mision es adivinar la siguiente palabra: {guiones}')
    print(f'Estas son tus vidas {vidas}, intenta adivinar antes que se acaben')
    while p_adivinada != palabra:
        if can_vidas > 0:
            intento = input('Ingresa una letra: ').lower()
            if intento in abecedario and len(intento) == 1:
                intentos.append(intento)
                if intento not in adivinar:
                    can_vidas -= 1
                    vidas.pop()
                    print(f'{intento} no esta en la palabra\nPerdiste una vida te quedan {can_vidas} {vidas}')
                elif intento in adivinar:
                    for l in adivinar:
                        if l == intento:                        
                            index = adivinar.index(intento)
                            g_adivinar[index] = intento
                            adivinar[index] = 'X'
                            p_adivinada = ''.join(g_adivinar)
                        else:
                            pass
                    print(f'Letras intentadas: {intentos}')
                print(p_adivinada)
            else:
                print('Ingrese una letra valida')
        elif can_vidas == 0:
            return (f'Perdiste se acabaron las vidas - La palabra era {palabras}')
    return (f'Has ganado - Felicitaciones {nombre.capitalize()}')

print(ahorcado(palabra,guion))