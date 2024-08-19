# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 13:09:21 2023

@author: Santi
"""

def propagar(l):
    
    #primero reviso hacia delante
    i = 0
    prop = l.copy()
    while i < len(prop)-1:
        if prop[i] == 1:
            if prop[i+1] != -1:
                prop[i+1] = 1
        i += 1
    r = len(prop)-1
    while r > 0:
        if prop[r] == 1:
            if prop[r-1] != -1:
                prop[r-1] = 1
        r -= 1
    return prop

propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
propagar([ 0, 0, 0, 1, 0, 0])
propagar([ -1, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 1])
propagar([ 1, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, -1])
propagar([ 1, 0, 0,0, -1, 0, 0, 0,0, 0, 0, 0, 1])
propagar([ 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0])
propagar([ -1, 0, 0, -1])

## chat gpt
def propagar(fosforos):
    n = len(fosforos)
    propagados = fosforos.copy()
    for i in range(n):
        if propagados[i] == 1:
            j = i - 1
            while j >= 0 and fosforos[j] == 0:
                propagados[j] = 1
                j -= 1
            j = i + 1
            while j < n and fosforos[j] == 0:
                propagados[j] = 1
                j += 1
    return propagados

propagar([ -1, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 1])


