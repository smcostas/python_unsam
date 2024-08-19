# -*- coding: utf-8 -*-
"""
Created on Sat May 13 14:04:14 2023

@author: Santi
"""

import csv
import sys


def costo_camion(arch):

    costo_total = 0
    with open (arch, 'rt', encoding = 'utf8') as f:
        lines = csv.reader(f)
        next(lines)
        for i,line in enumerate(lines):
            try:
                costo_total += int(line[1])*float(line[2])
            except ValueError:
                print(f'hay un dato faltante en la linea {i}')
        #print(f'el costo total es: {costo_total:0.2f}')
    return costo_total





if len(sys.argv) == 2:
    n_csv = sys.argv[1]
else:
    n_csv = '../Data/camion.csv'


costo = costo_camion(n_csv)
print(f'el precio total es {costo:0.2f}')
