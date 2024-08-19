# -*- coding: utf-8 -*-
"""
Created on Sat May 13 14:28:27 2023

@author: Santi
"""

s = ('Manzanas', 100, 490.1)

fruta, cajones, precio = s
s = {
    'fruta': 'Manzana',
    'cajones': 100,
    'precio': 490.1
}

print(s['fruta'], s['cajones'])
s['precio']


s['precio'] = 75
s['restante'] = 15
s['fecha'] = '6/8/2020'

del s['restante']
del s['fecha']


import csv

f = open('../Data/camion.csv')

filas = csv.reader(f)

next(filas)

fila = next(filas)
fila

t = (fila[0], int(fila[1]), float(fila[2]))
t

costo = t[1]*t[2]
costo
print(f'{costo:0.2f}')


# las listas son de solo lectura
t[1] = 75
# para modificarla, la reemplazo por una nueva con el mismo nombre
t = (t[0], 75, t[2])

nombre, cajones, precio = t # desempaqueto tuplas
t = (nombre, 2*cajones, precio)
t


d = {
        'nombre' : fila[0],
        'cajones' : int(fila[1]),
        'precio'  : float(fila[2])
    }

print(d)

cost = d['cajones']*d['precio']

cost
d['cajones'] = 75
d['fecha'] = (14, 8, 2020)
d['cuenta'] = 12345

for k in d:
    print(f'k= {k}')
    
for k in d:
    print(f'{k} = {d[k]}')
    
items = d.items()
items

for k,v in d.items():
    print(k, '=' , v)
    
    
nuevos_items = [('nombre', 'Manzanas'), ('cajones', 100), ('precio', 490.1), ('fecha', (13, 8, 2020))]

d = dict(nuevos_items)

d
