# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:50:18 2023

@author: Santi
"""

'''
#%% primer ejerccion
f = open('Data/arboles.csv', 'rt')
data = f.read()
print(data)
f.close()
#%%
nombre_del_archivo = 'Data/arboles.csv'
with open(nombre_del_archivo, 'rt', encoding='utf8') as file:
    encabezados = next(file).split(',')
    for i,fila in enumerate(file):
        print(i, fila)
        

#%%
with open(nombre_del_archivo, 'rt', encoding='utf8') as file:
    encabezados = next(file).split(',')
    print(encabezados)
    for i,fila in enumerate(file):
        fila = fila.split(',')
        print(i, fila)
#%%

import os
os.getcwd()
os.chdir('C:/Users/Santi/ejercicios python unsam nuevo/Clase02')
with open('../Data/camion.csv', 'rt', encoding = 'utf8') as f:
    data = f.read() ## solo tiene sentido si el archivo es chico sino conviene leer linea por linea
data
print(data)
#%%
n_archivo = '../Data/camion.csv'
with open (n_archivo, 'rt', encoding = 'utf8') as f:
    for line in f: 
        print(line, end = '')
        

#%% 
with open (n_archivo, 'rt', encoding = 'utf8') as f:
    headers = next(f).split(',') # convierte una string en una list separando por , (csv)
    for line in f:
        row = line.split(',')
        print(row)
        
        
#%%

import os
os.getcwd()
os.chdir('C:/Users/Santi/ejercicios python unsam nuevo/Clase02')

n_archivo = '../Data/camion.csv'
costo_total = 0

with open (n_archivo, 'rt', encoding = 'utf8') as f:
    headers = next(f).split(',') # convierte una string en una list separando por , (csv)
    for line in f:
        row = line.split(',')
        costo_total = costo_total + int(row[1])*float(row[2])

print(f'el costo total es: {costo_total:0.2f}')
#%% ejercicio 2.3
n_archivo2 = '../Data/precios.csv'
with open (n_archivo2, 'rt', encoding = 'utf8') as precios:
    for line in precios:
        if 'Naranja' in line:
            line = line.split(',')
            print(f'el precio de la naranja es {float(line[1]):0.2f}')
            
#%%

import gzip

with gzip.open('../Data/camion.csv.gz', 'rt') as f:
        for line in f:
            print(line, end = '')
'''
#%% 2.6
'''
def costo_camion(arch):
    
    costo_total = 0
    with open (arch, 'rt', encoding = 'utf8') as f:
        next(f) # convierte una string en una list separando por , (csv)
        for line in f:
            row = line.split(',')
            costo_total += int(row[1])*float(row[2])
    print(f'el costo total es: {costo_total:0.2f}')
    return costo_total


n_archivo = '../Data/camion.csv'

costo = costo_camion(n_archivo)
print(f'el precio es {costo:0.2f}')
'''
#%% 2.8
'''
def costo_camion(arch):

    costo_total = 0
    with open (arch, 'rt', encoding = 'utf8') as f:
        next(f).split(',') # convierte una string en una list separando por , (csv)
        for i,line in enumerate(f):
            try:
                row = line.split(',')
                costo_total += int(row[1])*float(row[2])
            except ValueError:
                print(f'hay un dato faltante en la linea {i}')
        print(f'el costo total es: {costo_total:0.2f}')
    return costo_total


n_archivo = '../Data/camion.csv'
n_archivo2 = '../Data/missing.csv'
costo = costo_camion(n_archivo2)
print(f'el precio es {costo:0.2f}')

## opcion sin value error
def costo_camion(arch):

    costo_total = 0
    with open (arch, 'rt', encoding = 'utf8') as f:
        next(f).split(',') # convierte una string en una list separando por , (csv)
        for i,line in enumerate(f):
            row = line.split(',')
            if '' not in row:  ## es mejor usar if, por que si hay un dato que esta mal tipiado genera un valueError que si me interesa.
                costo_total += int(row[1])*float(row[2])
            else:
                print(f'hay un dato faltante en la linea {i}')
        print(f'el costo total es: {costo_total:0.2f}')
    return costo_total
n_archivo2 = '../Data/missing.csv'
costo_camion(n_archivo2)

'''


#%%
#2.9 Con modulo csv
import csv
import os
os.chdir('C:/Users/Santi/ejercicios python unsam nuevo/Clase02')
def costo_camion(arch):

    costo_total = 0.0
    with open (arch, 'rt', encoding = 'utf8') as f:
        lines = csv.reader(f)
        next(lines)
        for i,line in enumerate(lines):
            try:
                costo_total += int(line[1])*float(line[2])
            except ValueError:
                print(f'hay un dato faltante en la linea {i}')
        print(f'el costo total es: {costo_total:0.2f}')
    return costo_total

n_archivo = '../Data/camion.csv'
n_archivo2 = '../Data/missing.csv'
costo = costo_camion(n_archivo)
print(f'el precio es {costo:0.2f}')

#%%
def costo_camion(arch):

    costo_total = 0
    with open (arch, 'rt', encoding = 'utf8') as f:
        f = csv.reader(f)
        next(f) # convierte una string en una list separando por , (csv)
        for i,line in enumerate(f):
            print(i)
            if '' not in line:  ## es mejor usar if, por que si hay un dato que esta mal tipiado genera un valueError que si me interesa.
                costo_total += int(line[1])*float(line[2])
            else:
                print(f'hay un dato faltante en la linea {i}')
        print(f'el costo total es: {costo_total:0.2f}')
    return costo_total
n_archivo2 = '../Data/missing.csv'
costo_camion(n_archivo2)


n_archivo = '../Data/camion.csv'
n_archivo2 = '../Data/missing.csv'
costo = costo_camion(n_archivo)
print(f'el precio es {costo:0.2f}')


