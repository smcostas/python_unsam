# -*- coding: utf-8 -*-
"""
Created on Tue May 11 19:39:30 2021

@author: Santi
"""

import os
def listar_png(directorio):
    '''
    la funcion recibe un directorio
    e imprime la precencia de archivos png
    en ese directorio y los subdirectorios en el
    '''
    ...
    
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if '.png' in name or '.PNG' in name:
                print(name)
    ...

if __name__ == '__main__':
    import sys
    listar_png(sys.argv)


