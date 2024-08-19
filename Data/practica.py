# -*- coding: utf-8 -*-
"""
Created on Sun May 21 18:54:23 2023

@author: Santi
"""

a = [2,4,5,6,7]
b = a
del a[2:4]
a[1:3] = [10,11,12]
b = 2


columnas = ['nombre', 'cajones', 'precio']
valores = ['Pera', 100, 490.1 ]
pares = zip(columnas, valores)
# ('nombre','Pera'), ('cajones',100), ('precio',490.1)
d = dict(zip(columnas, valores))

for n in range(10):            # Contar 0 ... 9
        print(n, end=' ')
        

for n in range(10,0,-1):       # Contar 10 ... 1
        print(n, end=' ')
        
        
