# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 13:12:59 2021

@author: Santi
"""

def costo_camion(nombre_archivo):
    ...
    from informe import leer_camion
    camion = leer_camion(nombre_archivo)
    gasto_total = sum([lote['cajones'] * lote['precio'] for lote in camion])
    print('Costo total:', gasto_total)
    return gasto_total ## por si lo quiero usar mas adelante.
    ...

def main(argv):
    camion = argv[1] ## cuando lea de con solo descarto el primer argumento (0)
    costo_camion(camion)
import sys    
if __name__ == '__main__':
    main(sys.argv)