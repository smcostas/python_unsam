# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:45:22 2021

@author: Santi
"""
## 5.10
import numpy as np
import random
def crear_album(figus_total):
    '''crea un album vacío de n figuritas = figus
    total'''
    n = np.zeros(figus_total, dtype=np.int64)
    return n
##5.11
def album_incompleto(A):
    if  A.min() == 0:
        return True
    return False
##5.12
def comprar_figus(figus_total):
    ''' ingresa un entero con el numero de figuritas
     y devuelve la posición de la figurita que te toca'''
    figu = random.randint(0,figus_total-1)
    return figu

## 5.13
def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    n = 0
    while album_incompleto(album) == True:
        figu = comprar_figus(figus_total)
        n+=1
        album[figu] += 1 
    return n
paquetes = cuantas_figus(25)
paquetes
##5.14
n_repeticiones = 1000
cantidad = np.array([cuantas_figus(6) for i in range(n_repeticiones)])
media = np.mean(cantidad)
print(media)

## 5.15 
def experimento_figus(n_repeticiones, figus_total):
    cantidad = np.array([cuantas_figus(figus_total) for i in range(n_repeticiones)])
    media = np.mean(cantidad)
    return media

experimento_figus(100,670)

## 5.16
paquete = [random.randint(0,669) for i in range(5)]
paquete

##5.17
def comprar_paquete(figus_total, figus_paquete):
    paquete = [random.randint(0,figus_total-1) for i in range(figus_paquete)]
    return paquete

paquete = comprar_paquete(200,5)

## 5.18

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    paquetes = 0
    while album_incompleto(album) == True:
        paquete = comprar_paquete(figus_total, figus_paquete)
        paquetes += 1
        for figu in paquete:
            album[figu] += 1
    return paquetes

cuantos_paquetes(670,5)
## 5.19
n_repeticiones = 100
cantidad = np.array([cuantos_paquetes(670,5) for i in range(n_repeticiones)])        
media = np.mean(cantidad)
print(f' para un album de 670 figuritas, comprando paquetes de 5 figuritas, se necesita comprar en promedio {int(media)}')

##
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5
import matplotlib.pyplot as plt
plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()

## 5.20
cantidad = np.array([cuantos_paquetes(670,5) for i in range(n_repeticiones)])
album_con_850 = np.array([1 for i in cantidad if i <= 850])
prob = len(album_con_850)/n_repeticiones
prob = (cantidad <=850).sum()/n_repeticiones
print(f'la probabilidad de llenar un album de 670 figus cob menos de 850 paquetes es de {prob}')
## 5.21
plt.hist(cantidad,bins=20)
## 5.22
cantidad = np.sort(cantidad)
prob90 = cantidad[int(len(cantidad)*0.9)-1]
prob90
prob = (cantidad <=prob90).sum()/n_repeticiones
prob
print(f' se necesitan {prob90} paquetes para tener un 90 por ciento de chances de llenar el album')

## 5.23
## sin reposición
def comprar_paquete(figus_total, figus_paquete):
    figus = [i for i in range(figus_total)]
    paquete = random.sample(figus, k = figus_paquete)
    return paquete

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    paquetes = 0
    while album_incompleto(album) == True:
        paquete = comprar_paquete(figus_total, figus_paquete)
        paquetes += 1
        for figu in paquete:
            album[figu] += 1
    return paquetes

comprar_paquete(670,5)
cantidad = np.array([cuantos_paquetes(670,5) for i in range(n_repeticiones)])        
media = np.mean(cantidad)
media
prob = (cantidad <=850).sum()/n_repeticiones
prob
cantidad = np.sort(cantidad)
cantidad
prob90 = cantidad[int(len(cantidad)*0.9)-1]
prob90
prob = (cantidad <=prob90).sum()/n_repeticiones
prob

## 5.24
def comprar_paquete(figus_total, figus_paquete):
    paquete = [random.randint(0,figus_total-1) for i in range(figus_paquete)]
    return paquete
def cuantos_paquetes_amigues(figus_total, figus_paquete):
    album1 = crear_album(figus_total)
    album2 = crear_album(figus_total)
    album3 = crear_album(figus_total)
    album4 = crear_album(figus_total)
    album5 = crear_album(figus_total)
    paquetes = 0
    while album_incompleto(album1) and  album_incompleto(album2) and album_incompleto(album3) and album_incompleto(album4) and album_incompleto(album5) == True:
        paquete = comprar_paquete(figus_total, figus_paquete)
        paquetes += 1
        for figu in paquete:
            if album1[figu] == 0:
                album1[figu] = 1
            elif album2[figu] == 0:
                album2[figu] = 1
            elif album3[figu] == 0:
                album3[figu] = 1
            elif album4[figu] == 0:
                album4[figu] = 1
            elif album5[figu] == 0:
                album5[figu] = 1
    return paquetes
cuantos_paquetes_amigues(670,5)
cantidad = np.array([cuantos_paquetes_amigues(670,5) for i in range(n_repeticiones)]) 
media = np.mean(cantidad)
media
