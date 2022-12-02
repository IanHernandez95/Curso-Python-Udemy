# def suma(**kwargs):
#     # print(type(kwargs)) dict
#     total = 0

#     for clave,valor in kwargs.items():
#         print(f'{clave} = {valor}')
#         total += valor

#     return total

# print(suma(x=3,y=5,z=2))

def prueba(num1, num2, *args, **kwargs):

    print(f'Primer valor es {num1}')
    print(f'Segundo valor es {num2}')
    
    for a in args:
        print(f'a = {a}')

    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')

args = [1321,15,2,12]
kwars = {
    'x':'65','z':'153','y':'dos'
}

prueba(15,50,*args,**kwars)