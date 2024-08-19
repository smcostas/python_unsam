# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 11:47:01 2021

@author: Santi
"""
import random
def generar_punto():
    x = random.random()
    y = random.random()
    return x,y
generar_punto()
N = 100000
M = []
puntos_a = ([generar_punto() for i in range(N)])
for x, y in puntos_a:
    if x**2 + y**2 < 1:
        M.append(x)
M = len(M)
pi = 4*M/N
print(f'pi es = {pi:0.4f}')        
