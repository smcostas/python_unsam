# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 17:23:38 2021

@author: Santi
"""

def ord_burbujeo(lista):
    '''Ordena una lista de elementos según el método de burbujeo.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada.'''
    n = len(lista)-1
    cambios = True
    while n > 0 and cambios:
        cambios = False
        for i in range (n):
            if lista[i] > lista[i+1]:
                p = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = p
                cambios = True
        n -= 1

lista = [4,2,3,4,5]

ord_burbujeo(lista)
# es n*n - chirolas
#lista = [5,3,2,1,0]
#ord_burbujeo(lista)
#lista_1 = [1, 2, -3, 8, 1, 5]
#ord_burbujeo(lista_1)
#lista_2 = [1, 2, 3, 4, 5]
#ord_burbujeo(lista_2)
#lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
#ord_burbujeo(lista_3)
#lista_4 = [10, 8, 6, 2, -2, -5]
#lista_5 = [2, 5, 1, 0]


def ord_burbujeo_rec(lista):
    '''Ordena una lista de elementos según el método de burbujeo de modo recursivo.
       (tiene una funcion auxiliar para impedir modificar parametros)
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada.'''
    def fun_aux(lista, cambios = True, n = len(lista)-1):
        if len(lista) <= 1: ## el caso de que se pase una lista vacia o de un solonumero
            cambios = False
        if cambios:
            cambios = False
            for i in range(n):
                if lista[i] > lista [i+1]:
                    p = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = p
                    cambios = True
                fun_aux(lista, cambios = cambios, n = n-1)
    fun_aux(lista)



#import random

#lista = [random.randint(1,1000) for i in range(100)]
#ord_burbujeo_rec(lista)
#lista = [5,4,3,2,1]
#ord_burbujeo_rec(lista)
#lista = [1]
#ord_burbujeo_rec(lista)
#lista = []
#ord_burbujeo_rec(lista)

