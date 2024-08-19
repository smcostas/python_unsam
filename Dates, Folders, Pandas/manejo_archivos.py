# -*- coding: utf-8 -*-
"""
Created on Tue May 11 17:19:15 2021

@author: Santi
"""

import os
os.getcwd()
os.chdir('C:/Users/Santi/Desktop/back up disco/python/program_en_python/Ejercicios/ejercicios_python/Clase08')  
os.chdir('../data')

os.chdir('..') 
os.listdir('../ejercicios_python/Data')

os.mkdir('test') 
os.mkdir(os.path.join('test', 'carpeta')) 
os.listdir('test')

os.chdir('test')
os.rename('carpeta','carpeta_nueva') 

os.chdir('..')  
os.listdir('test') 
os.rename(os.path.join('test', 'carpeta_nueva'), os.path.join('test','carpeta_vieja'))
os.listdir('test')
os.rename(os.path.join('test','carpeta_vieja'), 'carpeta_vieja')
os.listdir('test')
os.listdir('carpeta_vieja')
os.chdir('otra_carpeta') 


import os
for root, dirs, files in os.walk("."):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))
      
#%%
import os
import datetime
import time
os.chdir('../Clase06')
camino = './rebotes.py'
stats_archivo = os.stat(camino)

print(time.ctime(stats_archivo.st_atime))

fecha_acceso = datetime.datetime(year = 2017, month = 9, day = 21, hour = 19, minute =51, second = 0)
fecha_modifi = datetime.datetime(year = 2012, month = 9, day = 24, hour = 12, minute =9, second = 24)

ts_acceso = fecha_acceso.timestamp()
ts_modifi = fecha_modifi.timestamp()

os.utime(camino, (ts_acceso, ts_modifi))

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))