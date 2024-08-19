# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
dado = random.randint(1,6)
tirada=[]
for i in range(5):
    tirada.append(random.randint(1,6)) 

print(tirada)


def tirada(n):
    tirada = [random.randint(1,6) for i in range(n)]
    return tirada


print(tirada(5))

def es_generala (tirada):
    r = False
    if len(tirada) == 5:
        r = all([val == tirada[0] for val in tirada])
    return r


es_generala(tirada(5))

N = 1000000
G = sum([es_generala(tirada(5)) for i in range(N)])
prob = G/N
#print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
#print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

realprob = 1/6*1/6*1/6*1/6
print(f'la verdadera probabilidad de sacar generala servida es {realprob:.6f}.')


## codigo 2
### generala jugando
import random
from collections import Counter

def tirada(n):
    tirada = [random.randint(1,6) for i in range(n)]
    return tirada

def es_generala (tirada):
    r = False
    if len(tirada) == 5:
        r = all([val == tirada[0] for val in tirada])
    return r


### si son todos distintos tirar todo de vuelta
def generala (selecionar_dado = True):
    tiradas = 0
    seleccionados = []
    r = False
    while (tiradas <= 3) and (r == False):
        t = tirada(5-len(seleccionados))
        tiradas += 1
        if es_generala(t):
            seleccionados = t
            r = es_generala(seleccionados)
        if not r:
            if len(seleccionados) == 0:
                if len(set(t)) != len([t]):
                    c = Counter(t)
                    e,n = c.most_common(1)[0]
                    seleccionados = [e for i in range(n)]
                else:
                    if selecionar_dado:
                        dado = random.randint(0,4)
                        seleccionados = t[dado]
            else:
                if seleccionados[0] in t:
                    for e in t:
                        if e in seleccionados:
                            seleccionados.append(e)
                    r = es_generala(seleccionados)
                else:
                    if len (seleccionados) < len(t):
                        c_s = Counter(seleccionados)
                        c_t = Counter(t)
                        e_s , n_s = c_s.most_common(1)[0]
                        e_t , n_t = c_t.most_common(1)[0]
                        if n_t > n_s:
                            seleccionados = [e_t for i in range(n_t)]
    return r



generala()
N = 1000000
G = sum([generala() for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala jugando.')
print(f'Podemos estimar la probabilidad de sacar generala jugando {prob:.6f}.')
