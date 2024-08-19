# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 09:44:26 2021

@author: Santi
"""
"""
'''
#%%
import csv
## 6.6
def parse_csv(nombre_archivo):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        # Lee los encabezados
        headers = next(rows)
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            registro = dict(zip(headers, row))
            registros.append(registro)

    return registros

camion = parse_csv('../Data/camion.csv')
camion

#%%
# 6.7
import csv

def parse_csv(nombre_archivo, select = None):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select: ## si selec tiene valores
            indices = [encabezados.index(nombre_columna) for nombre_columna in select] ## extraes en una lista los indices de select en encabezados 
            encabezados = select ## si select tiene valores entonces reducis el encabezado a esos valores
        else:
            indices = [] ##si no hay select entonces lista vacia (no hay indices)

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices: ## si indices tiene valores entonces filtra sino fila es completa
                fila = [fila[index] for index in indices]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros

parse_csv('../Data/camion.csv', select=['nombre','cajones'])
#%%
#6.8
import csv

def parse_csv(nombre_archivo, select = None, types = None):
    
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    se puede transformar las columnas seleccionadas a str, int y float.
    
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select: ## si selec tiene valores
            indices = [encabezados.index(nombre_columna) for nombre_columna in select] ## extraes en una lista los indices de select en encabezados 
            encabezados = select ## si select tiene valores entonces reducis el encabezado a esos valores
        else:
            indices = [] ##si no hay select entonces lista vacia (no hay indices)

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices: ## si indices tiene valores entonces filtra sino fila es completa
                fila = [fila[index] for index in indices]
            if types:
                fila = [func(val) for func, val in zip(types, fila) ]
            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros

camion = parse_csv('../Data/camion.csv', types=[str, int, float])
camion
cajones_lote = parse_csv('../Data/camion.csv', select=['nombre', 'cajones'], types=[str, int])
cajones_lote
'''
#%%
"""
import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    se puede transformar las columnas seleccionadas a str, int y float.
    se puede leer una tabla sin encabezados, en ese caso no se puede seleccionar un subconjunto
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        registros = []
        if has_headers:
        # Lee los encabezados del archivo
            encabezados = next(filas)
    
            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
            if select: ## si selec tiene valores
                indices = [encabezados.index(nombre_columna) for nombre_columna in select] ## extraes en una lista los indices de select en encabezados 
                encabezados = select ## si select tiene valores entonces reducis el encabezado a esos valores
            else:
                indices = [] ##si no hay select entonces lista vacia (no hay indices)
    
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices: ## si indices tiene valores entonces filtra sino fila es completa
                    fila = [fila[index] for index in indices]
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        else:
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                # Armar el diccionario
                registro = tuple(fila)
                registros.append(registro)
                

    return registros


precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)
precios
cajones_lote = parse_csv('../Data/camion.csv', select=['nombre', 'cajones'], types=[str, int])
cajones_lote
