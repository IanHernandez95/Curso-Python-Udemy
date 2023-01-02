import bs4
import requests

# resultado = requests.get('https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html')

# sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

# # parrafo_especial = sopa.select('p')[3].getText()
# # print(parrafo_especial)

# columna_lateral = sopa.select('.post p')
# # print(columna_lateral)
# for p in columna_lateral:
#     print(p.getText())

resultado = requests.get('https://www.escueladirecta.com/courses')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes = sopa.select('.course-box-image')[0]['src']
print(imagenes)

imagen_curso1 = requests.get(imagenes)

f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso1.content)
f.close()