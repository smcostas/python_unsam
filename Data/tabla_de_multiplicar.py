#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 16:38:32 2023

@author: user12021
"""

### talba de multiplicar 3.17

numeros = []
for i in range(10):
    numeros.append(i)
     
lista_tuplas = []
for numero in numeros:
    tupla = [0]
    n = 0
    for _ in range(9):
        n += numero
        tupla.append(n)
    tupla = tuple(tupla)
    lista_tuplas.append(tupla)
    
encabezado = lista_tuplas[1] 
a,b,c,d,e,f,g,h,i,j = encabezado
print('    ','%2s %2s %2s %2s %2s %2s %2s %2s %2s %2s' % (a,b,c,d,e,f,g,h,i,j))
print('----------------------------------')
s = 0
for a,b,c,d,e,f,g,h,i,j in lista_tuplas:
    print(f'{s}:  ','%2s %2s %2s %2s %2s %2s %2s %2s %2s %2s' % (a,b,c,d,e,f,g,h,i,j))
    s += 1
    



### version chat gpt


numeros = list(range(10))

lista_tuplas = []
for numero in numeros:
    tupla = [0]
    n = 0
    for _ in range(9):
        n += numero
        tupla.append(n)
    lista_tuplas.append(tuple(tupla))

encabezado = lista_tuplas[1]
print('    ', ' '.join(f'{i:2}' for i in encabezado))
print('----------------------------------')
for s, tupla in enumerate(lista_tuplas):
    print(f'{s}:  ', ' '.join(f'{i:2}' for i in tupla))
    
    
    
numeros = list(range(10))

lista_listas = []
for numero in numeros:
    sublista = [0]
    n = 0
    for _ in range(9):
        n += numero
        sublista.append(n)
    lista_listas.append(sublista)

encabezado = lista_listas[1]
print('    ', ' '.join(f'{i:2}' for i in encabezado))
print('----------------------------------')
for s, sublista in enumerate(lista_listas):
    print(f'{s}:  ', ' '.join(f'{i:2}' for i in sublista))