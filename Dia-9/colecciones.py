# from collections import Counter
# from collections import defaultdict
from collections import namedtuple


# numero = [5,5,1,6,5,5,1,1,5,2,2,8,8,8,2,6,6,6,6,7]
# print(Counter(numero))
# print(Counter('mississippi'))
# frase = 'al pan pan y al vino vino'
# print(Counter(frase.split()))

# serie = Counter([1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4])
# print(list(serie))

# mi_dic = defaultdict(lambda: 'nada')

# mi_dic['uno'] = 'verde'
# print(mi_dic['dos'])
# print(mi_dic)

Persona = namedtuple('persona', ['nombre','altura','peso'])
ariel = Persona('Ariel',1.76,79)

print(ariel.altura)