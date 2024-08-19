# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 11:05:13 2023

@author: Santi
"""

a = [2,3,[100,101],4]
b = list(a)
b
def tup(nombre):
    tuple((int(i) for i in nombre.split('/')))

a = [13,12,11]
b = [2*x if x > 12 else x for x in a]

## fijando ideas

import csv
f = open('../Data/dowstocks.csv')

rows = csv.reader(f)

headers = next(rows)
row = next(rows)

types = [str, float, tuple, str, float, float, float, float, int]


converted = [func(val) if '/' not in val else func(map(int,val.split('/'))) for func, val in zip(types, row)] ## map aplica una funcion a cada elemento de una secuencia
record = dict(zip(headers, converted))



diccionarios = []
for row in rows:
    converted = [func(val) if '/' not in val else func(map(int,val.split('/'))) for func, val in zip(types, row)]
    record = dict(zip(headers, converted))
    diccionarios.append(record)
    
diccionarios = [dict(zip(headers, [func(val) if '/' not in val else tuple(map(int,val.split('/'))) for func, val in 
                                   zip(types, row)])) for row in rows]

f.close()
