# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:28:35 2023

@author: Santi
"""

import csv
#import os
#os.chdir('ejercicios python unsam nuevo/Clase04')

def leer_camion(arch):

    camion = []
    with open (arch, 'rt', encoding = 'utf8') as f:
        lines = csv.reader(f)
        encabezados = next(lines)
        for i,line in enumerate(lines, start = 2):
            try:
                lote = dict(zip(encabezados, line))
                lote['cajones'] = int(lote['cajones'])
                lote['precio'] = float(lote['precio'])
                camion.append(lote)
            except ValueError :
                print(f'hay un dato faltante en la linea {i}')
    return camion


n_archivo = '../Data/camion.csv'
n_archivo2 = '../Data/missing.csv'

camion = leer_camion(n_archivo)
camion[0]
total = 0.0
for s in camion:
        total += s['cajones']*s['precio']
        
print(total)

print(camion)



def leer_precios(arch):
    precios = {}
    with open (arch, 'rt', encoding = 'utf8') as f:
        lines = csv.reader(f)
        for i,line in enumerate(lines, start =  1):
            if '' in line:
                print(f'hay un dato faltante en la linea {i}')
            elif len(line) != 2:
                print(f'la linea {i} no cumple con el formato len == 2')
            else:
                precios[line[0]] = float(line[1])
    return precios


precios = leer_precios('../Data/precios.csv')

precios['Naranja']
precios['Mandarina']

def balance(camion, precios):
    camion = leer_camion(camion)
    precios = leer_precios(precios)
    
    gasto_total= 0.0
    venta_total = 0.0
    for lote in camion:
        gasto_total += lote['cajones']* lote['precio']
        fruta = lote['nombre']
        if fruta in precios:
            venta_total += precios[fruta] * lote['cajones']
    balance = venta_total - gasto_total
    print(f'La ganancia neta fue {balance:0.2f}')
    return balance


precios  = '../Data/precios.csv'
camion = '../Data/camion.csv'
camion_fecha = '../Data/fecha_camion.csv'
ganancia = balance(camion_fecha, precios)



camion = leer_camion('../Data/camion.csv')


#%% 
from collections import Counter

tenencias = Counter()

for s in camion:
    tenencias[s['nombre']] += s['cajones']
    
tenencias['Naranja']
tenencias['Mandarina']

tenencias.most_common(3)


camion2 = leer_camion('../camion2.csv')

tenencias2 = Counter()
for tenencia in camion2:
    tenencias2[tenencia['nombre']] += tenencia['cajones'] 
    
    
combinada  = tenencias + tenencias2
print(combinada)
#%%
#ejercicios 4.8
camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')


costo_total = sum([lote['precio']*lote['cajones'] for lote in camion])
print(costo_total)

gasto_total= sum([precios[lote['nombre']] * lote['cajones'] for lote in camion])
print(gasto_total)


mas100 = [lote for lote in camion if lote['cajones'] > 100]
myn = [lote for lote in camion if lote['nombre'] in ['Mandarina', 'Naranja']]
myn

costo10k = [lote for lote in camion if lote['cajones']*lote['precio'] > 10000]
costo10k

nombre_cajones = [(lote['nombre'],lote['cajones']) for lote in camion]

#4.11
f = open('../Data/fecha_camion.csv')

rows = csv.reader(f)

headers = next(rows)

select = ['nombre', 'cajones', 'precio']

indices = [headers.index(ncolumna) for ncolumna in select]

row = next(rows)
record = {ncolumna: row[index] for ncolumna, index in zip(select, indices)}
record


camion = [{ncolumna: row[index] for ncolumna, index in zip(select, indices)} for row in rows]
