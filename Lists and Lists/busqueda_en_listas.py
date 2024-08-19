# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 12:22:38 2023

@author: Santi
"""
def buscar_u_elemento(lista,u):
    '''
    la funcion busca en la lista el elemento u,y devuelve la última pos
    en la que se enceuntra. Si no está devuelve -1
    parametros : lista = una lista
    u = elemento a buscar
    '''
    pos = -1
    for i,e in enumerate(lista):
        if e == u:
            pos = i
    return pos

buscar_u_elemento([1,2,3,2,3,4],1)
buscar_u_elemento([1,2,3,2,3,4],2)
buscar_u_elemento([1,2,3,2,3,4],3)
buscar_u_elemento([1,2,3,2,3,4],5)

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # inicializo con el primer elemento de la lista.
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m


maximo([1,2,7,2,3,4])
maximo([1,2,3,4])
maximo([-5,4])
maximo([-5,-4])

"""
def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
     # inicializo con el primer elemento de la lista.
    i = 0
    m = lista[0]
    while i < len(lista): # Recorro la lista y voy guardando el mayor
        if lista[i] > m:
            m = lista[i]
        i +=1
    return m

maximo([1,2,7,2,3,4])
maximo([1,2,3,4])
maximo([-5,4])
maximo([-5,-4])
"""

def minimo(lista):
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # inicializo con el primer elemento de la lista.
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e < m:
            m = e
    return m


minimo([1,2,7,2,3,4])
minimo([1,2,3,4])
minimo([-5,4])
minimo([-5,-4])
