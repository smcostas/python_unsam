# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:06:32 2021

@author: Santi
"""

def donde_insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve la posición donde insertar para que siga ordenada si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    izq = 0
    der = len(lista) - 1
    while izq <= der :
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio
            return pos
            # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1
            pos = medio# descarto mitad derecha
        else:
            izq = medio + 1
            pos = medio
    if x > lista[len(lista)-1]:
        pos = len(lista)
    elif pos == 0:
        pos += 1
    elif x < lista[0]:
        pos = 0
    return pos
    
#%%
def insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve la posición donde insertar para que siga ordenada si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    izq = 0
    der = len(lista) - 1
    while izq <= der :
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio
            return pos
            # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1
            pos = medio# descarto mitad derecha
        else:
            izq = medio + 1
            pos = medio
    if x > lista[len(lista) - 1]:
        lista.append(x)
    elif x < lista[0]:
        lista.insert(0, x)
    elif medio == 0:
        pos= medio+1
        lista.insert(pos,x)
    else:
        pos = pos 
        lista.insert(pos,x)
    return pos, lista
donde_insertar([0,1,4,5,6], 0, verbose = True)
insertar([0,2,3,4],1)
insertar([-1,2,3,5],-13)
