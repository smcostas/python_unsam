# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 15:48:18 2021

@author: Santi
"""

## 7.4
def parse_csv(lines, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    se puede transformar las columnas seleccionadas a str, int y float.
    se puede leer una tabla sin encabezados, en ese caso no se puede seleccionar un subconjunto
    '''
    import csv
    filas = csv.reader(lines) ## la diferencia es que en vez de abrir un archivo csv le das el archivo ya leido lo que le da flexibilidad
    registros = []
    if select and has_headers == False: ## ejercicio 7
        raise RuntimeError("Para seleccionar, necesito encabezados.")
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

        for i, fila in enumerate(filas): # ejercicio 7 agregar try y value error
            try: # Para esto tu ve poner enumerate para marcar la fila que no se puede leer
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
            except ValueError as e:
                if  silence_errors:
                    continue

                else:
                    print(f'fila {i}:  No pude convertir {fila}')
                    print(f'fila {i}:  Motivo: {e}')                        
    else:
        for i, fila in enumerate(filas):
            try:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                # Armar la tupla
                registro = tuple(fila)
                registros.append(registro)
            except ValueError as e:
                if silence_errors:
                    continue
                else:
                    print(f'fila {i}:  No pude convertir {fila}')
                    print(f'fila {i}:  Motivo: {e}')
            

    return registros

