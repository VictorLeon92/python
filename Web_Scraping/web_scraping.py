import bs4
import requests

'''
https://escueladirecta-blog.blogspot.com/
'''

resultado = requests.get('https://justbecauseyes.com')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print(sopa.select('title')[0].getText())

'''
Sintaxis de captura de elementos

soup.select('div') -> Devuelve todos los elementos con etiquetas div
soup.select('#estilo') -> Devielve el elemento que tenga la id estilo
soup.select('.cosa'') ->Muestra los elementos con clase cosa
soup.select('div span') -> devuelve elementos que tenga la estructura exacta de ser un div con un span en su interior
'''
# Recopilar todos los elementos p de una columna con clase content, y mostrar solo el texto de cada elemento
columna_lateral = sopa.select('.content p')
for p in columna_lateral:
    print(p.getText())

# Recopilar imágenes
imagenes = sopa.select('.course-box-image')[0]['src'] # Recoge solo la url de la imagen

# Descargar imagen
imagen_curso_1 = requests.get(imagenes)
f = open('mi-imagen.jpg', 'wb')
f.write(imagen_curso_1.content)
f.close()