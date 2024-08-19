# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 11:23:08 2021

@author: Santi
"""

import rebotes
import hipoteca
import informe_funciones
import fileparse

help(fileparse)
camion = fileparse.parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
camion
lista_precios = fileparse.parse_csv('../Data/precios.csv', types = [str, float], has_headers = False)
lista_precios
precios = dict(lista_precios)
precios
precios['Naranja']

from fileparse import parse_csv
camion = parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
camion
