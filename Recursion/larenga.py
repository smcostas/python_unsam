# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 09:33:43 2021

@author: Santi
"""

# triangulo de pascal 

def pascal(n,k):
    
    if (n < 1 ) or (k == 0) or (n == k):
        valor = 1
    else:
        valor = pascal(n-1,k-1) + pascal(n-1,k)
    return valor


pascal(2, 1)
pascal(3,2)
pascal(5,2)
pascal(5,5)
