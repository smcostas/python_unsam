# -*- coding: utf-8 -*-
"""
Created on Wed May 12 09:57:51 2021

@author: Santi
"""

import pandas as pd
import os
import seaborn as sns
import numpy as np

idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
s2 = s1.cumsum()

s2.plot()

w = 5 # ancho en minutos de la ventana
s3 = s2.rolling(w).mean()
s3.plot()

df_series_23 = pd.DataFrame([s2, s3]).T  # armo un dataframe con ambas series
df_series_23.plot()
print(df_series_23)


horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']
df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)
df_walks
df_walks.plot()
## datos suavizados
w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() # datos suavizados
nsuav = ['S_' + n for n in nombres]
df_walk_suav.columns = nsuav # cambio el nombre de las columnas
                             # para los datos suavizados
df_walk_suav.plot()

#os.chdir('C:/Users/Santi/Desktop/back up disco/python/program_en_python/Ejercicios/ejercicios_python/Clase08')
directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df_lineal = pd.read_csv(fname)

cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal.columns
df_lineal = df_lineal[cols_sel]
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]

df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
sns.boxplot(data = df_lineal_seleccion, y = 'altura_arbol', x = 'nombre_cientifico')

# pairplot

sns.pairplot(data = df_lineal_seleccion, hue = 'nombre_cientifico')

## ejercicio 8.9
