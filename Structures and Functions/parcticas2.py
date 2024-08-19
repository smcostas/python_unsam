# -*- coding: utf-8 -*-
"""
Created on Sun May 14 10:21:08 2023

@author: Santi
"""
import csv
import os
os.chdir('C:/Users/Santi/ejercicios python unsam nuevo/Clase02')

registros = []  # Empezamos con una lista vacía

with open('../Data/camion.csv', 'rt') as f:
    next(f) # Saltear el encabezado
    for line in f:
        row = line.split(',')
        registros.append((row[0], int(row[1]), float(row[2])))
        
registros


precios = {}  # Empezamos con un diccionario vacío

with open('../Data/precios.csv', 'rt', encoding = 'utf8') as f:
    f = csv.reader(f)
    for line in f:
        if line:
            precios[line[0]] = float(line[1])
        
precios

if 'Naranja' in precios:
    print('esta')



## conjuntos
citricos = { 'Naranja','Limon','Mandarina' }
# Alternativamente podemos escribirlo así:
citricos = set(['Naranja', 'Limon', 'Mandarina'])

nombres = ['Naranja', 'Manzana', 'Pera', 'Naranja', 'Pera', 'Banana']
## podemos eliminar duplicados utilizando conjuntos
nombres = set(nombres)
nombres
