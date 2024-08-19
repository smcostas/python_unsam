# -*- coding: utf-8 -*-
"""
Created on Sun May 14 11:15:19 2023

@author: Santi
"""

import csv
import os
from pprint import pprint
os.chdir('C:/Users/Santi/ejercicios python unsam nuevo/Clase02')

'''
def leer_camion(arch):

    camion = []
    with open (arch, 'rt', encoding = 'utf8') as f:
        lines = csv.reader(f)
        next(lines)
        for i,line in enumerate(lines):
            try:
                lote = (line[0], int(line[1]), float(line[2]))
                camion.append(lote)
            except ValueError:
                print(f'hay un dato faltante en la linea {i}')
    return camion


n_archivo = '../Data/camion.csv'
n_archivo2 = '../Data/missing.csv'
leer_camion(n_archivo)
leer_camion(n_archivo2)
'''

#%% 2.16

def leer_camion(arch):

    camion = []
    with open (arch, 'rt', encoding = 'utf8') as f:
        lines = csv.reader(f)
        next(lines)
        for i,line in enumerate(lines, start = 2):
            lote = {}
            if len(line) == 3:
                try:
                    lote['nombre'] = line[0]
                    lote['cajones'] = int(line[1])
                    lote['precio'] = float(line[2])
                    camion.append(lote)
                except ValueError :
                    print(f'hay un dato faltante en la linea {i}')
    return camion


n_archivo = '../Data/camion.csv'
n_archivo2 = '../Data/missing.csv'

camion = leer_camion(n_archivo2)
camion[0]
total = 0.0
for s in camion:
        total += s['cajones']*s['precio']
        
print(total)

print(camion)
pprint(camion)


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

ganancia = balance(camion, precios)
