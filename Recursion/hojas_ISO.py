# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:51:50 2021

@author: Santi
"""
## 11.13 
def size(n):
    '''
     tiene que ser un entero mayor o igual a 0 (caso base)
     devuelve el tamaño de la hoja a partir de A1 en forma de tupla con ancho, largo
    '''
    if n == 0:
        a = 841 ## ancho de a1
        l = 1189 ## largo de a1
        tamaño = (a,l)
    else:
        tamaño = size(n-1)
        a = tamaño[1]//2 
        l = tamaño[0]
        tamaño = (a,l)
    return tamaño

size(4)
size(5)
size(1)
size(2)
size(0)
