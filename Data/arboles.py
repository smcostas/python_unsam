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
#os.chdir('C:/Users/Santi/ejercicios python unsam nuevo/Clase03')

def leer_parque(arch, parque):
    '''
    

    Parameters
    ----------
    arch : string con la ruta al archivo csv
.
    parque : string con el nombre exacto del parque que se desea obtener info
    como figura en el csv

    Returns lista de diccionarios con la informacion del parque especificado. Un diccionario
    por cada árbol en el parque
    -------.

    '''
    lista_parque = []
    with open(arch, 'rt', encoding = 'utf8') as f:
        f = csv.reader(f)
        encabezados = next(f)
        for fila in f:
            if parque in fila:
                arbol = dict(zip(encabezados,fila))
                arbol['altura_tot'] = float(arbol['altura_tot'])
                arbol['inclinacio'] = int(arbol['inclinacio'])
                lista_parque.append(arbol)
    return lista_parque

archivo = '../arbolado-en-espacios-verdes.csv'
parque = 'GENERAL PAZ'


general_paz = leer_parque(archivo, parque)
len(general_paz)

#%% 3.19

def especies(lista_arboles):
    '''

    Parameters
    ----------
    lista_arboles : lista de diccionarios generada con la funcion leer_parque

    Returns una coleccion (elementos unicos) con las especies de árboles escritas en nombre común presentes
    en el parque (riqueza)
    -------
    None.

    '''
    
    lista_especies = []
    for arbol in lista_arboles:
        especie = arbol['nombre_com']
        lista_especies.append(especie)
    lista_especies = set(lista_especies)
    return lista_especies

lista_especies = especies(general_paz)
len(lista_especies)

#%% 3.20

def contar_ejemplares(lista_arboles):
    '''

    Parameters
    ----------
    lista_arboles : lista de diccionarios (arboles) generada con la función leer_parque
    
    Returns un objeto del modulo collecionts (funcion counter) que tiene el numereo de ejemplares por especies
    -------
    None.

    '''
    
    total_ejemplares = Counter()
    for arbol in lista_arboles:
        spp = arbol['nombre_com']
        total_ejemplares[spp] += 1
    return total_ejemplares


cont = contar_ejemplares(general_paz)


#%%
def most_common_arboles (arch, lista_parques, n = 5):
    
    arboles_comunes = []
    for p in lista_parques:
        parque = leer_parque(arch, p)
        ejemplares = contar_ejemplares(parque)
        common_trees = ejemplares.most_common(n)
        arboles_comunes.append(common_trees)
    return arboles_comunes
    

archivo = '../arbolado-en-espacios-verdes.csv'
lista_parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
arboles_comunes = most_common_arboles(archivo, lista_parques)



#%% chat gpt
'''def most_common_arboles (arch, lista_parques, n = 5):
    
    arboles_comunes = []
    for p in lista_parques:
        parque = leer_parque(arch, p)
        ejemplares = contar_ejemplares(parque)
        common_trees = ejemplares.most_common(n)
        arboles_comunes.append([f'{tree}: {count}' for tree, count in common_trees])
    
    data = zip(*arboles_comunes)
    header = ''.join([f"{parque:<30s}" for parque in lista_parques])
    print(header)
    for trees in data:
        row = ''.join([f"{tree:<30s}" for tree in trees])
        print(row)
    return [arboles_comunes, data]
        
'''

#%%
def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles:
        spp = arbol['nombre_com']
        if especie == spp:
            alturas.append(arbol['altura_tot'])
    return alturas


alturas_gp = obtener_alturas(general_paz, 'Jacarandá')
alturas_la = obtener_alturas(leer_parque(archivo, 'ANDES, LOS'), 'Jacarandá')
alturas_cent = obtener_alturas(leer_parque(archivo, 'CENTENARIO'), 'Jacarandá')
lista_alturas = [alturas_gp, alturas_la, alturas_cent]


for parque in lista_alturas:
    print(max(parque), mean(parque))


#%%

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        spp = arbol['nombre_com']
        if especie == spp:
            inclinaciones.append(arbol['inclinacio'])
    return inclinaciones

inclinaciones_jgp = obtener_inclinaciones(general_paz, 'Jacarandá')

#%% 
def especimen_mas_inclinado(lista_arboles):
    spps = especies(lista_arboles)
    inclinaciones_maximas = []
    for especie in spps:
            inclinacion = obtener_inclinaciones(lista_arboles, especie)
            inclinacion = (max(inclinacion), especie)
            inclinaciones_maximas.append(inclinacion)
    return max(inclinaciones_maximas)

especimen_mas_inclinado(general_paz)
especimen_mas_inclinado(leer_parque(archivo, 'ANDES, LOS'))
especimen_mas_inclinado(leer_parque(archivo, 'CENTENARIO'))


#%%

def especie_promedio_mas_inclinada(lista_arboles):
    spps = especies(lista_arboles)
    inclinaciones_pmaxima = []
    for especie in spps:
            inclinacion = obtener_inclinaciones(lista_arboles, especie)
            inclinacion = ((sum(inclinacion)/len(inclinacion)), especie)
            inclinaciones_pmaxima.append(inclinacion)
    return max(inclinaciones_pmaxima)


especie_promedio_mas_inclinada(leer_parque(archivo, 'ANDES, LOS'))


## toda la ciudad.

#3.24
def leer_parques(arch):
    '''
    

    Parameters
    ----------
    arch : string con la ruta al archivo csv


    Returns lista de diccionarios con la informacion del parque especificado. Un diccionario
    por cada árbol en la ciudad
    -------.

    '''
    lista_parques = []
    with open(arch, 'rt', encoding = 'utf8') as f:
        f = csv.reader(f)
        encabezados = next(f)
        for fila in f:
            arbol = dict(zip(encabezados,fila))
            arbol['altura_tot'] = float(arbol['altura_tot'])
            arbol['inclinacio'] = int(arbol['inclinacio'])
            arbol['long'] = float(arbol['long'])
            arbol['lat'] = float(arbol['lat'])
            lista_parques.append(arbol)
    return lista_parques

archivo = '../Data/arbolado-en-espacios-verdes.csv'


buenos_aires = leer_parques(archivo)
especie_promedio_mas_inclinada(leer_parques(archivo))

#%%

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        spp = arbol['nombre_com']
        if especie == spp:
            inclinaciones.append((arbol['inclinacio'], arbol['long'], arbol['lat'], spp))
    return inclinaciones



#%% 
def especimen_mas_inclinado(lista_arboles):
    spps = especies(lista_arboles)
    inclinaciones_maximas = []
    for especie in spps:
            inclinacion = max(obtener_inclinaciones(lista_arboles, especie))
            inclinaciones_maximas.append(inclinacion)
    return max(inclinaciones_maximas)




especimen = especimen_mas_inclinado(buenos_aires)


#%% forma a mi entender más eficiente

def especimen_mas_inclinado(lista_arboles):
    indiv = lista_arboles[0]
    for arbol in lista_arboles:
        if arbol['inclinacio'] > indiv['inclinacio']:
            indiv = arbol
    return indiv

especimen = especimen_mas_inclinado(buenos_aires)
