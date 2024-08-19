# -*- coding: utf-8 -*-
"""
Created on Wed May 19 10:48:58 2021

@author: Santi
"""

import  lote
a = lote.Lote('Pera', 100, 490.10)

a.nombre
a.cajones
a.precio

b = lote.Lote('Manzana', 50, 122.34)
c = lote.Lote('Naranja', 75, 91.75)

b.cajones * b.precio

c.cajones * c.precio

lotes = [a, b, c]

for c in lotes:
     print(f'{c.nombre:>10s} {c.cajones:>10d} {c.precio:>10.2f}')


s = lote.Lote('Pera', 100, 490.10)
s.costo()    

s.vender(25)
s.cajones

import fileparse
with open('../Data/camion.csv') as lineas:
     camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
     
camion = [ lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
camion

sum([c.costo() for c in camion])

