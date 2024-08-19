# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:14:11 2023

@author: Santi
"""
#%%
#3.8
import csv
import os
os.chdir('C:/Users/Santi/ejercicios python unsam nuevo/Clase03')
def costo_camion(arch):

    costo_total = 0
    with open (arch, 'rt', encoding = 'utf8') as f:
        f = csv.reader(f)
        encabezados = next(f) # convierte una string en una list separando por , (csv)
        for i,line in enumerate(f, start = 2):
            record = dict(zip(encabezados,line))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += precio*ncajones
            except ValueError:
                print(f'Fila {i} : no puede interpretar:{line}')
        print(f'el costo total es: {costo_total:0.2f}')
    return costo_total



n_archivo2 = '../Data/missing.csv'
costo_camion(n_archivo2)


n_archivo = '../Data/camion.csv'
n_archivo2 = '../Data/missing.csv'
n_archivo3 = '../Data/fecha_camion.csv'
costo_camion(n_archivo)
costo_camion(n_archivo2)
costo_camion(n_archivo3)


