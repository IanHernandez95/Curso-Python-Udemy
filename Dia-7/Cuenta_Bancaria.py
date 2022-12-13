import os


class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'El cliente {self.nombre} {self.apellido} tiene en su cuenta N° {self.numero_cuenta} la cantidad de {self.balance} pesos'
    
    def depositar(self,deposito):
        self.balance += deposito

    def retirar(self,retiro):
        if self.balance >= retiro:
            self.balance -= retiro
        else:
            print('Saldo insuficiente')


def crear_cliente():
    nombre = input('Ingrese nombre del Cliente: ')
    apellido = input('Ingrese apellido del Cliente: ')
    numero_de_cuenta = input('Ingrese Numero de cuenta del Cliente: ')
    cliente_nuevo = Cliente(nombre,apellido,numero_de_cuenta)
    return cliente_nuevo

def inicio():
    usuario = crear_cliente()
    os.system('cls')
    loop = True
    print(usuario)
    while loop:
        print('''
        Ingrese 1 - Para Depositar
        Ingrese 2 - Para Retirar
        Ingrese 3 - Para Salir
        ''')
        opcion = int(input('Su opcion: ' ))
        os.system('cls')
        if opcion == 1:
            monto = int(input('Cuanto desea Depositar: '))
            usuario.depositar(monto)
            print(f'El saldo nuevo es {usuario.balance}')
        elif opcion == 2:
            monto = int(input('Cuanto desea Retirar: '))
            usuario.retirar(monto)
            print(f'El saldo nuevo es {usuario.balance}')
        elif opcion == 3:
            loop = False
            print('Gracias por Operar')
        else:
            print('Ingrese una opcion valida')

inicio()
