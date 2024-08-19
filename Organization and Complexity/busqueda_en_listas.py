# -*- coding: utf-8 -*-

#%%
def buscar_u_elemento (lista, u):
    '''
    busca la ultima aparicion del elemento u 
    y devuelve el índice. Si no está devuelve -1
    '''
    pos = -1
    i = len(lista) - 1
    while i >= 0:
        if u == lista[i]: 
            pos = i
            break
        i -= 1
    return pos

buscar_u_elemento([1,2,3,2,3,4],1)
buscar_u_elemento([1,2,3,2,3,4],2)
buscar_u_elemento([1,2,3,2,3,4],3)
buscar_u_elemento([1,2,3,2,3,4],5)

def buscar_u_elemento2 (lista, u):
    '''
    busca la ultima aparicion del elemento u 
    y devuelve el índice. Si no está devuelve -1
    '''
    pos = -1
    i = len(lista) - 1
    for z in lista:
        if u == lista[i]: 
            pos = i
            break
        i -= 1
    return pos

buscar_u_elemento2([1,2,3,2,3,4],1)
buscar_u_elemento2([1,2,3,2,3,4],2)
buscar_u_elemento2([1,2,3,2,3,4],3)
buscar_u_elemento2([1,2,3,2,3,4],5)

#%%
'''def maximo (lista):

    m = 0
    for e in lista:
        if e > m:
            m = e
    return m

maximo([1,2,7,2,3,4])
maximo([1,2,3,4])
maximo([-5,4])
maximo([-5,-4])
'''

def maximo (lista):
    '''
    devuelve el maximo de una lista
    lista debe ser no vacia
    '''
    m = lista[0]
    for e in lista:
        if e > m:
           m = e 
    return m

maximo([-4,-5])
maximo([-5,-4])
maximo([1,2,7,2,3,4])
maximo([1,2,3,4])
#%%
def minimo (lista):
    m = lista[0]
    for e in lista:
        if e < m:
           m = e 
    return m

minimo([-4,-5])
minimo([-5,-4])
minimo([1,2,7,2,3,4])
minimo([1,2,-7,2,3,4])
