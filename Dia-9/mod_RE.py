import re



# texto = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online'


# patron = 'ayuda'

# # busqueda = re.findall(patron, texto)
# # print(busqueda)

# for hallazgo in re.finditer(patron,texto):
#     print(hallazgo.span())

# texto = 'llama al 536-631-1256 ya mismo'
# patron = r'\d\d\d-\d\d\d-\d\d\d\d'
# patron = r'\d{3}-\d{3}-\d{4}'
# patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

# resultado = re.search( patron, texto )
# print(resultado.group(3))

# clave = input('clave: ')
# patron = r'\D{1}\w{7}'

# chek = re.search(patron, clave)
# print(chek)

texto = 'No atendemos los martes por la tarde'

# buscar = re.search(r'lunes|martes',texto)
# buscar = re.search(r'...demos...',texto)
# buscar = re.search(r'^\D',texto)
# buscar = re.search(r'\D$',texto)
buscar = re.findall(r'[^\s]+',texto)
print(buscar)