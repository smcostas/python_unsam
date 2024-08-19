# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 13:12:59 2021

@author: Santi
"""
'''
## 9.4
from informe import leer_camion
def costo_camion(nombre_archivo):
    ...
    camion = leer_camion(nombre_archivo)
    gasto_total = sum([lote.costo() for lote in camion])
    print('Costo total:', gasto_total)
    return gasto_total ## por si lo quiero usar mas adelante.
    ...

def main(argv):
    camion = argv[1] ## cuando lea de con solo descarto el primer argumento (0)
    costo_camion(camion)
import sys    
if __name__ == '__main__':
    main(sys.argv)
    
    
#costo_camion('../Data/camion.csv')
'''
#%%
## ejercicio 10.2
import informe

def costo_camion(nombre_archivo):
    ...
    camion = informe.leer_camion(nombre_archivo)
    return  camion.precio_total()
    ...

def main(argv):
    camion = argv[1] ## cuando lea de con solo descarto el primer argumento (0)
    print(costo_camion(camion))
    
import sys    
if __name__ == '__main__':
    main(sys.argv)

