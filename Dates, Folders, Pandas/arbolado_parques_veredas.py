# -*- coding: utf-8 -*-
"""
Created on Wed May 12 11:48:59 2021

@author: Santi
"""

import pandas as pd
import os
import seaborn as sns

directorio = '../data'
archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'
archivo_parques = 'arbolado.csv'
fn_veredas = os.path.join(directorio,archivo_veredas)
fn_parques = os.path.join(directorio,archivo_parques)
## lectura de archivos
df_veredas = pd.read_csv(fn_veredas)
df_parques = pd.read_csv(fn_parques)

## tipa en veredas
col_selec_veredas = ['nombre_cientifico','diametro_altura_pecho', 'altura_arbol']
df_veredas = df_veredas[col_selec_veredas]
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'].isin(['Tipuana tipu'])].copy()
df_tipas_veredas = df_tipas_veredas.rename(columns={"diametro_altura_pecho": "diametro", "altura_arbol": "altura"})
df_tipas_veredas = df_tipas_veredas.assign(Ambiente = 'vereda')

## tipa en parques
col_selec_parques = ['nombre_cie','diametro', 'altura_tot']
df_parques = df_parques[col_selec_parques]
df_tipas_parques = df_parques[df_parques['nombre_cie'].isin(['Tipuana Tipu'])].copy()
df_tipas_parques = df_tipas_parques.rename(columns={"altura_tot": "altura"})
df_tipas_parques = df_tipas_parques.assign(Ambiente = 'parque')

## concat
selec  = ['altura','diametro','Ambiente']
df_tipas = pd.concat([df_tipas_veredas[selec], df_tipas_parques[selec]])

## grafico
#alutra
sns.boxplot(data = df_tipas, y = 'altura', x = 'Ambiente')
# diametro
sns.boxplot(data = df_tipas, y = 'diametro', x = 'Ambiente')

## si se puede hacer una funcion o poner todas las especies en una misma matriz y subsetear por especie a la hora de hacer los graficos


