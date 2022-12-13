# class Animal:
    
#     def __init__(self, edad, color):
#         self.edad = edad
#         self.color = color

#     def nacer(self):
#         print('Este animal ha nacido')

#     def hablar(self):
#         print('Este animal emite un sonido')


# class Pajaro(Animal):

#     def __init__(self, edad, color, altura_vuelo):
#         super().__init__(edad,color)
#         self.altura_vuelo = altura_vuelo

#     def hablar(self):
#         print('Pio')

#     def volar(self, metros):
#         print(f'El pajaro vuela {metros} metros')


# piolin  = Pajaro(3,'amarillo',60)
# animal = Animal(5,'negro')

# # piolin.hablar()
# piolin.volar(100)


class Padre:
    
    def hablar(self):
        print('Hola')

class Madre:

    def reir(self):
        print('ja ja')

    def hablar(self):
        print('que tal')

class Hijo(Padre, Madre):
    pass 

class Nieto(Hijo):
    pass


nieto = Nieto()

# nieto.hablar()
# nieto.reir()

print(Nieto.__mro__)