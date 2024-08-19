# -*- coding: utf-8 -*-
"""
Created on Mon May 10 20:27:23 2021

@author: Santi
"""

#%%
import datetime

def segundos_vividos(cadena_con_fecha):
    ''' a una cadena con fecha de nacimiento con formato
        dd/mm/yyyy y devuelve el tiempo vivido en segundos
    '''
    date_object = datetime.datetime.strptime(cadena_con_fecha, '%d/%m/%Y')
    date_today = datetime.datetime.now()
    delta_tiempo = abs(date_today - date_object)
    segundos_v = delta_tiempo.total_seconds()
    return segundos_v

print('segundos vividos:', segundos_vividos('15/04/1993'))

