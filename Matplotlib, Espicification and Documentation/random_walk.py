# -*- coding: utf-8 -*-
"""
Created on Wed May  5 10:05:17 2021

@author: Santi
"""
## ejercicio 7.9
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja la curva
plt.xticks([]), plt.yticks([]) # saca las marcas

plt.subplot(2, 3, 4) # define la primera de abajo, que sería la cuarta si fuera una grilla regular de 2x3
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5) # define la segunda de abajo, que sería la quinta si fuera una grilla regular de 2x3
plt.plot([0,1],[1,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 6) # define la tercera de abajo, que sería la sexta figura si fuera una grilla regular de 2x3
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])

plt.show()

## ejercicio 7.10

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000

ran = [x for x in range(1,13)]
walks = [randomwalk(N) for r in ran]

## obtengo la que más se aleja
minimo = walks[0]
maximo = walks[0]
larga = walks[0]
for walk in walks:
    if min(walk) <= min(minimo):
        minimo = walk
    if max(walk) >= max(maximo):
        maximo = walk
    if abs(max(maximo)) >= abs(min(minimo)):
        larga = maximo
    else:
        larga = minimo

## obtengo la que menos se aleja

cerca = walks[0]
comp_max = 10000 ## valor absoluto a comprar
comp_min = 10000 ## valor absoluto a comprar
for walk in walks:
    maximo = abs(max(walk))
    minimo = abs(min(walk))
    if  maximo > minimo: ### compara cual es el valor que mas se aleja para luego comparar entre los que mas se alejan
        if maximo < comp_max:
            comp_max = maximo
        if comp_max < comp_min:
            comp_min = comp_max ## como estoy seleccionado sobre ese valo ambas comparaciones tienen que ser el valor minimo hasta el momento 
            cerca = walk
    else: ### compara cual es el valor que mas se aleja para luego comparar entre los que mas se alejan cual es el que menos se aleja 
        if minimo < comp_min:
            comp_min = minimo
        if comp_min < comp_max:
            comp_max = comp_min
            cerca = walk
       
## todos juntos
for walk in walks:
    plt.subplot(2, 1, 1)
    plt.plot(walk)
    plt.ylim(-700, 700)
    plt.xticks([])
    plt.ylabel("Distancia al origen")
    plt.title("12 Caminatas al azar")
    
## el mas lejano 
plt.subplot(2,2,3)
plt.plot(larga)
plt.ylim(-700, 700)
plt.xticks([])
plt.title("la que mas se aleja")
## el mas cercano
plt.subplot(2,2,4)
plt.ylim(-700, 700)
plt.yticks([])
plt.xticks([])
plt.plot(cerca)
plt.title("la que menos se aleja")

plt.show()



   
