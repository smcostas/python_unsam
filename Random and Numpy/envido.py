# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 19:32:12 2021

@author: Santi
"""

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]
naipes

import random
#random.seed(31415)
mano = random.sample(naipes,k=3)

    
## envido 33

def envido33():
    mano = random.sample(naipes,k=3)
    ## expreso todas las posibilidades de obtener 33
    if (mano[0][1] == mano[1][1]) and (mano[0][0] == 6) and (mano[1][0] == 7):
        return True    
    if (mano[0][1] == mano[1][1]) and (mano[0][0] == 7) and (mano[1][0] == 6):
        return True
    if (mano[0][1] == mano[2][1]) and (mano[0][0] == 6) and (mano[2][0] == 7):
        return True    
    if (mano[0][1] == mano[2][1]) and (mano[0][0] == 7) and (mano[2][0] == 6):
        return True        
    if (mano[1][1] == mano[2][1]) and (mano[1][0] == 6) and (mano[2][0] == 7):
        return True    
    if (mano[1][1] == mano[2][1]) and (mano[1][0] == 7) and (mano[2][0] == 6):
        return True
    return False

N = 1000000
G = sum([envido33() for i in range(N)])
prob33 = G/N 
print(f'la probabilidad de obtener 33 en un envido es {prob33:.3f}')
def envido32():
    ## expreso todas las posibilidades de obtener 32
    mano = random.sample(naipes,k=3)
    if (mano[0][1] == mano[1][1]) and (mano[0][0] == 5) and (mano[1][0] == 7):
        return True    
    if (mano[0][1] == mano[1][1]) and (mano[0][0] == 7) and (mano[1][0] == 5):
        return True    
    if (mano[0][1] == mano[2][1]) and (mano[0][0] == 5) and (mano[2][0] == 7):
        return True    
    if (mano[0][1] == mano[2][1]) and (mano[0][0] == 7) and (mano[2][0] == 5):
        return True
    if (mano[1][1] == mano[2][1]) and (mano[1][0] == 5) and (mano[2][0] == 7):
        return True    
    if (mano[1][1] == mano[2][1]) and (mano[1][0] == 7) and (mano[2][0] == 5):
        return True  
    return False

N = 1000000
G = sum([envido32() for i in range(N)])
prob32 = G/N 
print(f'la probabilidad de obtener 31 en un envido es {prob32:.3f}')
def envido31():
    mano = random.sample(naipes,k=3)
    ## expreso todas las posibilidades de obtener 31
    if (mano[0][1] == mano[1][1]) and ((mano[0][0] == 4) and (mano[1][0] == 7) or ((mano[0][0] == 5) and (mano[1][0] == 6))):
        return True    
    if (mano[0][1] == mano[1][1]) and ((mano[0][0] == 7) and (mano[1][0] == 4) or ((mano[0][0] == 6) and (mano[1][0] == 5))):
        return True    
    if (mano[0][1] == mano[2][1]) and ((mano[0][0] == 4) and (mano[2][0] == 7) or ((mano[0][0] == 5) and (mano[2][0] == 6))):
        return True    
    if (mano[0][1] == mano[2][1]) and ((mano[0][0] == 7) and (mano[2][0] == 4) or ((mano[0][0] == 6) and (mano[2][0] == 5))):
        return True
    if (mano[1][1] == mano[2][1]) and ((mano[1][0] == 4) and (mano[2][0] == 7) or ((mano[1][0] == 5) and (mano[2][0] == 6))):
        return True    
    if (mano[1][1] == mano[2][1]) and ((mano[1][0] == 7) and (mano[2][0] == 4) or ((mano[1][0] == 6) and (mano[2][0] == 5))):
        return True  
    return False

N = 1000000
G = sum([envido31() for i in range(N)])
prob31 = G/N
print(f'la probabilidad de obtener 31 en un envido es {prob31:.3f}')
