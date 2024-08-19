# -*- coding: utf-8 -*-
"""
Created on Sat May 13 16:50:04 2023

@author: Santi
"""
#%%
## una opción, crear un diccionario vacio y agregar, palabra por palabra.

def dic_ger(palabras):


    '''
    

    Parameters
    ----------
    palabras : TYPE
        DESCRIPTION.

    Returns
    -------
    dic : TYPE
        DESCRIPTION.

    '''
    dic = {}
    for palabra in palabras:
        palabra = palabra.lower()
        ger = ''
        len(palabra)
        'a' in palabra
        for l in palabra:
            if l in 'aeiou':
                ger = ger + l + "p" + l
            else:
                ger = ger+l
        dic[palabra] = ger
    return dic

lista = ['banana', 'manzana', 'mandarina']


dic = dic_ger(lista)

#%%
## otra opciones es crear una lista de tuplas y luego trasformarlas
def dic_ger(palabras):

    '''
    

    Parameters
    ----------
    palabras : TYPE
        DESCRIPTION.

    Returns
    -------
    dic : TYPE
        DESCRIPTION.

    '''
    dic = []
    for palabra in palabras:
        palabra = palabra.lower()
        ger = ''
        len(palabra)
        'a' in palabra
        for l in palabra:
            if l in 'aeiou':
                ger = ger + l + "p" + l
            else:
                ger = ger+l
        dic.append((palabra, ger))
    dic = dict(dic)
    return dic

lista = ['banana', 'manzana', 'mandarina']
dic_ger(lista)
