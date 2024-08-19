# -*- coding: utf-8 -*-
"""
Created on Thu May 25 16:09:06 2023

@author: Santi
"""

#%%
#3.18

import csv
import os
import math
from collections import Counter
from statistics import mean
os.chdir('C:/Users/Santi/ejercicios python unsam nuevo/Clase04')


#Ejercicio 4.15: Lectura de todos los árboles
def leer_arboles(leer_archivo):
    arboleda= []
    with open (leer_archivo, 'rt', encoding= 'utf-8') as f:
        rows= csv.reader(f)
        header= next(rows)
        for fila in rows:
            arbol= dict(zip(header, fila))
            arboleda.append(arbol)
    return arboleda

arboleda= leer_arboles('../Data/arbolado-en-espacios-verdes.csv')


###4.18




#Ejercicio 4.16: Lista de altos de Jacarandá
H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

#Ejercicio 4.17: Lista de altos y diámetros de Jacarandá
H_D= [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

#Ejercicio 4.18: Diccionario con medidas

def medidas_de_especies(especies,arboleda):
    diccionario = {clave: [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == clave]for clave in especies}
    return diccionario

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
dics = medidas_de_especies(especies, arboleda)

dics['Eucalipto']

        