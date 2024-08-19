#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:14:08 2023

@author: user12021
"""

import csv


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


'''
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
'''
## 3.16 

def hacer_informe(camion,precios):
    precios = leer_precios(precios)
    camion = leer_camion(camion)
    informe = []
    #headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    #nombre, cajones, precio, cambio = headers
    for lote in camion:
        fruta = lote['nombre']
        if fruta in precios:
            cajones = lote['cajones']
            precio = precios[fruta]
            cambio = precio - lote['precio']
            entrada = (fruta, cajones, precio, cambio)
            informe.append(entrada)
    return informe
'''
for r in informe:
    print(r)
for r in informe:
    print('%10s %10d %10.2f %10.2f' % r)
'''
def formato(informe):

    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    nombre, cajones, precio, cambio = headers
    print(f'{nombre:>10s} {cajones:>10s} {precio:>10s} {cambio:>10s}')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        #precio = '$' + str(round(precio,2))
        precio = '$' + '%0.2f' % precio
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')


precios = '../Data/precios.csv'
camion = '../Data/camion.csv'


informe = hacer_informe(camion, precios)

formato(informe)
