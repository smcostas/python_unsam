# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:23:19 2021

@author: Santi
"""

def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio] == e:
            res = True
        elif lista[medio] > e:
            res = bbinaria_rec(lista[:medio],e)
        else:
            res = bbinaria_rec(lista[medio:],e)
        # completar

    return res

bbinaria_rec([1,2,4,5], 2)
bbinaria_rec([1,2,4,5], 4)
bbinaria_rec([1,2,4], 4)
bbinaria_rec([0,1,2,3,4], 0)