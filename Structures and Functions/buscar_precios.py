# -*- coding: utf-8 -*-
"""
Created on Mon May  8 18:02:24 2023

@author: Santi
"""

#%% ejercicio 2.7

import os
os.chdir('C:/Users/Santi/ejercicios python unsam nuevo/Clase02')


def buscar_precios(n_archivo, fruta, alarma = True):
    with open (n_archivo, 'rt', encoding = 'utf8') as precios:
        try:
            for line in precios:
                if fruta in line:
                    line = line.split(',')
                    precio = float(line[1])
                    break
            if alarma:
                print(f'el precio de la {fruta} es {precio:0.2f}')
            return precio
                    
        except NameError:
            if alarma:
                print(f'{fruta} no está en la lista')
            
n_archivo2 = '../Data/precios.csv'
fruta = 'Naranja'
buscar_precios(n_archivo2, 'Kale', alarma = False)

buscar_precios(n_archivo2, 'Frambuesa', alarma = False)


#%% segun chat gpt es mas elegante este código.
def buscar_precios(n_archivo, fruta, verbose = True):
    with open (n_archivo, 'rt', encoding = 'utf8') as precios:
        precio = None
        for line in precios:
            if fruta in line:
                line = line.split(',')
                precio = float(line[1])
                break
        if verbose:
            if precio: ## los objetos None son evaluados como False
                print(f'el precio de la {fruta} es {precio:0.2f}')
            else:
                print(f'{fruta} no está en la lista')
        return precio
            
n_archivo2 = '../Data/precios.csv'

buscar_precios(n_archivo2, 'Kale', verbose = True)

buscar_precios(n_archivo2, 'Frambuesa', verbose = True)
