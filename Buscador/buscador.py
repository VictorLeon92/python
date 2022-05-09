import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()

ruta = 'C:\\Users\\Programación\\PycharmProjects\\Dia 9\\Proyecto\\Mi_Gran_Directorio'
mi_patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
numeros_encontrados = []
archivos_encontrados = []

def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''


def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta,a),mi_patron)
            if resultado != '':
                numeros_encontrados.append(resultado.group())
                archivos_encontrados.append(a.title())


def mostrar_todo():
    indice = 0
    print('-'*50)
    print(f'Fecha de búsqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')
    for a in archivos_encontrados:
        print(f'{a}\t{numeros_encontrados[indice]}')
        indice += 1

    print('\n')
    print(f'Números encontrados: {len(numeros_encontrados)}')
    final = time.time()
    duracion = final - inicio
    print(f'Duración de la búsqueda: {math.ceil(duracion)}')
    print('-' * 50)


crear_listas()
mostrar_todo()