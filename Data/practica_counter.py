#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 12:41:47 2023

@author: user12021
"""

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for i,fila in enumerate(filas):
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
            registro[encabezado[0]] = i
    return camion


#%%
camion = leer_camion('../camion.csv')
pprint(camion)



precios = {
        'Pera' : 490.1,
        'Lima' : 23.45,
        'Naranja' : 91.1,
        'Mandarina' : 34.23
    }


lista = precios.items()
lista_precios = list(zip(precios.values(),precios.keys()))


min(lista_precios)
max(lista_precios)
sorted(lista_precios, reverse = True)



from collections import Counter

camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.1),
    ('Caqui', 150, 83.44),
    ('Naranja', 100, 45.23),
    ('Pera', 75, 572.45),
    ('Lima', 50, 23.15)
]

total_cajones = Counter()

for nombre,n_cajones, precio in camion:
    total_cajones[nombre] += n_cajones
    
total_cajones['Pera']
