# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 12:04:31 2023

@author: santi
"""
import random
from collections import Counter
# cumpleaños 
grupo = []
for i in range(30):
    grupo.append(random.randint(1,365)) 
    
def prob_sim_edades(n):
    iguales = []
    for i in range(n):
        grupo = []
        for i in range(30):
            grupo.append(random.randint(1,365))
        dias = Counter(grupo)
        dias = dias.most_common()
        frecuencias = [n for d,n in dias]
        if frecuencias[0] >= 2:
            iguales.append(True)
    prob = sum(iguales)/n
    return prob


prob_sim_edades(10000)


### modifico para calcular cuando la probabilidad de que se repita un cumple (e) supere a la probabilidad de que sean todos diferentes (f)
def prob_sim_edades(n,g):
    e = 0
    f = 0
    for i in range(n):
        grupo = []
        for i in range(g):
            grupo.append(random.randint(1,365))
        dias = Counter(grupo)
        dias = dias.most_common()
        frecuencias = [n for d,n in dias]
        if frecuencias[0] >= 2:
            e += 1
        else: #sean todos diferentes
            f += 1
    p = e/n
    q = f/n
    return (p,q) # devuelvo un tupla 

n_grupo = []
for _ in range(1000):
    g = 2 ## arranco con2 personas
    while True:
        p,q = prob_sim_edades(1000, g)
        if p > q:
            break
        g += 1
    n_grupo.append(g)
    
nmedia = sum(n_grupo)/1000
print(f'el tamaño de grupo usando 1000 simulaciones donde la probabilidad de repetir se vuelve mas alta que la de que sean diferentes es {nmedia} repitiendolo 1000 veces')