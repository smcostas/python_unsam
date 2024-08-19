# -*- coding: utf-8 -*-
"""
Created on Tue May 25 10:21:37 2021

@author: Santi
"""
"""
from vigilante import vigilar
import csv
'''
def parsear_datos(lines):
    rows = csv.reader(lines)
    return rows

if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)
'''        
def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]
        
def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 2])
    return rows

#if __name__ == '__main__':
lines = vigilar('../Data/mercadolog.csv')
rows = parsear_datos(lines)
for row in rows:
    print(row)
    
def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
        
def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

lines = vigilar('../Data/mercadolog.csv')
rows = parsear_datos(lines)
for row in rows:
    print(row)
    

def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila

import informe
import formato_tabla
camion = informe.leer_camion('../Data/camion.csv')
filas = parsear_datos(vigilar('../Data/mercadolog.csv'))
filas = filtrar_datos(filas, camion)

for fila in filas:
    print(fila)
"""
## encontre una forma en la que puedo sacar las funciones elegir columnas y  cambiar tipo, pero no logre hacerlo mediante expresiones generadores
import csv
import informe
import formato_tabla
from vigilante import vigilar

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
        
def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = ([row[index] for index in [0, 1, 2]] for row in rows)
    #rows = elegir_columnas(rows, [0, 1, 2])
    rows = ([func(val) for func, val in zip([str, float, int], row)] for row in rows)
    #rows = cambiar_tipo(rows, [str, float, int])
    rows = (dict(zip(['nombre', 'precio', 'volumen'], row)) for row in rows)
    return rows
'''
def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila
'''
#otra resolucion si saco hacer dics cambiar tipo y elegir columnas
'''def filtrar_datos(filas, nombres):
    
    #for fila in filas:
     #   for e in fila:
      #      if e in nombres:
       #         yield fila
'''

def ticker(camion_file, log_file, fmt = 'txt'):
    
    formateador = formato_tabla.crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    camion = informe.leer_camion(camion_file)
    filas = parsear_datos(vigilar(log_file))
    filas = (fila for fila in filas if fila['nombre'] in camion)
    #filas = ([fila for fila in filas if e in nombre] for e in fila)
    for fila in filas:
        fila = [fila['nombre'], str(fila['precio']), str(fila['volumen'])]
        formateador.fila(fila)
        
ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'txt')


