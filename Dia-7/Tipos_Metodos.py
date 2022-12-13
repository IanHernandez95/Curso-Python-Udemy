class Pajaro:
    
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    # Metodos de Instancia
    def piar(self):
        print('Pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pajaro a volado {metros} metros')
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f'El pajaro ahora es {self.color}')


    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)


    @staticmethod
    def mirar():
        print('El pajaro mira')

# piolin = Pajaro('amarillo','canario')

# piolin.pintar_negro()
# piolin.volar(50)

# Pajaro.poner_huevos(3)
# Pajaro.piar()
Pajaro.mirar()