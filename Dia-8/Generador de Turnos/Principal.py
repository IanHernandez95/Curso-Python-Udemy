import Numeros

def principal():

    print('Bienvenido a Farmacia Python')

    while True:
        print('1 - Perfumeria\n2 - Farmacia\n3 - Cosmetica')
        try:
            opcion = int(input('Ingrese su opcion: '))  
            if opcion == 1:
                Numeros.dec_perfumeria()
            elif opcion == 2:
                Numeros.dec_farmacia()
            elif opcion == 3:
                Numeros.dec_cosmetica()
            else:
                print('Ingrese una opcion Valida')
        except ValueError:
            print('Igrese una Opcion Valida')
        else:
            print('Otro Turno?')
            try:
                continuar = input('Ingrese S/N: ').upper()
                if continuar == 'N': 
                    print('Gracias por su Espera Visita')

            except:
                print('Opcion no valida ingrese S o N')


principal()