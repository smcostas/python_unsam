# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 09:57:41 2021

@author: Santi
"""

import time
import timeit as tt
import random
import numpy as np
import matplotlib.pyplot as plt
'''
tt.timeit('time.sleep(1)', number = 1)
tt.timeit('"-".join(str(n) for n in range(100))', number = 1)


tt.timeit('"-".join(str(n) for n in range(100))', number = 10000)
tt.timeit('"-".join([str(n) for n in range(100)])', number = 10000)
tt.timeit('"-".join(map(str, range(100)))', number = 10000)
'''

## ejercicio 12.8
#%%
#ord seleccion
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada. y devuelve el numero de comparaciones
       que le costo (simplificado)"""

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar

    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n) 
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        # reducir el segmento en 1
        n = n - 1


def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a

    for i in range(a + 1, b + 1):

        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max
#%%
# ord insercion
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada. y devuelve el número de comparaciones (simplificado) que utilizó"""

    for i in range(len(lista) - 1):

        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)


def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1]. y devuelve el numero de comparaciones
       que le costo reubicar
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v

#%%
def ord_burbujeo(lista):
    '''Ordena una lista de elementos según el método de burbujeo.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada.'''
    n = len(lista)-1
    cambios = True
    while n > 0 and cambios:
        cambios = False
        for i in range (n):
            if lista[i] > lista[i+1]:
                p = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = p
                cambios = True
        n -= 1

#%%
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado

#%%
#generar lista
def generar_lista(N):
    ''' genera una lista de largo N con numeros enteros del 1 al 1000
    pre = N debe ser un numero entero positivo
    post = lista con N elementos entre el 1 y el 1000 con posibilidad de repetidos
    '''
    
    lista = [random.randint(1,1000) for i in range(N)]
    return lista

#%%
def generar_listas(Nmax):
    ''' genera una lista de listas de largo Nmax, donde  cada lista sera de largo
    1 a Nmax-1
    pre = Nmax debe ser un entero positivo, si es 0 devolverá  una lista vacia
    post = lista dde listas de largo Nmax
    '''
    listas = []
    for N in range(1, Nmax):
        listas.append(generar_lista(N))
    return listas
#%%
def experimento_timeit_seleccion(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método
    de selección para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica el número de veces que repite el ordenamiento para cada lista.
    """
    tiempos_seleccion = []
    
    global lista
    
    for lista in listas:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = num, globals = globals())
        
        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        
    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    
    return tiempos_seleccion

def experimento_timeit_insercion(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método
    de selección para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica el número de veces que repite el ordenamiento para cada lista.
    """
    tiempos_seleccion = []
    
    global lista
    
    for lista in listas:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit('ord_insercion(lista.copy())', number = num, globals = globals())
        
        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        
    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    
    return tiempos_seleccion


def experimento_timeit_burbujeo(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método
    de selección para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica el número de veces que repite el ordenamiento para cada lista.
    """
    tiempos_seleccion = []
    
    global lista
    
    for lista in listas:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit('ord_burbujeo(lista.copy())', number = num, globals = globals())
        
        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        
    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    
    return tiempos_seleccion


def experimento_timeit_merge(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método
    de selección para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica el número de veces que repite el ordenamiento para cada lista.
    """
    tiempos_seleccion = []
    
    global lista
    
    for lista in listas:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit('merge_sort(lista.copy())', number = num, globals = globals())
        
        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        
    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    
    return tiempos_seleccion


listas = generar_listas(257)

t_seleccion = experimento_timeit_seleccion(listas.copy(), 100) ## creo que no es necesario ponerle listas.copy() pero por las dudas
t_insercion = experimento_timeit_insercion(listas.copy(), 100)
t_burbujeo = experimento_timeit_burbujeo(listas.copy(), 100)
t_merge = experimento_timeit_merge(listas.copy(), 100)

plt.plot(t_burbujeo, color = 'red', linestyle = 'dashed', label = 'burbujeo')
plt.plot(t_seleccion, color = 'blue', linestyle = 'dotted', label = 'seleccion')
plt.plot(t_insercion, color = 'green', label = 'insercion')
plt.plot(t_merge, color = 'black', label = 'merge')
plt.legend()
plt.show()