# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 12:55:14 2023

@author: Santi
"""

def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida.insert(0,e)
    return invertida


lista = [1, 2, 3, 4, 5]
invert = invertir_lista(lista)
lista2 = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
invert2 = invertir_lista(lista2)


def invertir_lista(lista):
    i = len(lista)
    invertida = []
    while i > 0: # Recorro la lista
        i -=1
        invertida.append(lista[i])
    return invertida

lista = [1, 2, 3, 4, 5]
invert = invertir_lista(lista)
lista2 = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
invert2 = invertir_lista(lista2)
