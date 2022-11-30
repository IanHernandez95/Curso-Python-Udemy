from random import randint

intentos = 0
numero_persona = 0
numero_secreto = randint(0,101)
nombre = input('Dime tu nombre: ')

print(f'Bueno {nombre}, he pensado un numero entre 1 y 100\nTiene 8 intentos para Adivinar')

while intentos < 8:
    numero_persona = int(input('¿Cuál es el numero?: '))
    intentos += 1   
    if numero_persona not in range(1,101):
        print('Tu numero no esta en rango de 1 a 100')
    elif numero_persona > numero_secreto:
        print('Mi numero es más bajo')
    elif numero_persona < numero_secreto:
        print('Mi numero es más alto')
    else:
        print(f'Felicitaciones {nombre}! Has adinicado en {intentos} intentos')
        break

if numero_persona != numero_secreto:
    print(f'Lo siento, se han agotado los intentos. El numero secreto era {numero_secreto}')
