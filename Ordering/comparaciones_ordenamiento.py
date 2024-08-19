# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 14:32:20 2021

@author: Santi
"""
#%%

import random
import numpy as np
import matplotlib.pyplot as plt
#%%
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada. y devuelve el numero de comparaciones
       que le costo (simplificado)"""

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    comparaciones = 0
    while n > 0:
        # posición del mayor valor del segmento
        p_comparaciones = buscar_max(lista, 0, n)
        p = p_comparaciones[0]
        comparaciones += p_comparaciones[1] ## en este ordenamiento el numero esta dado en mayor medida por la busqueda del maximo, luego realiza varias comparaciones mas que decidi decestimar 
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        # reducir el segmento en 1
        n = n - 1
    return comparaciones

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    comparaciones = 0
    for i in range(a + 1, b + 1):
        comparaciones += 1
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max, comparaciones

#%%

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada. y devuelve el número de comparaciones (simplificado) que utilizó"""
    comparaciones = 0
    for i in range(len(lista) - 1):
        comparaciones += 1
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            comparaciones += reubicar(lista, i + 1)
    return comparaciones

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1]. y devuelve el numero de comparaciones
       que le costo reubicar
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    comparaciones = 0
    while j > 0 and v < lista[j - 1]:
        comparaciones += 1
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v
    return comparaciones





#%%

def ord_burbujeo(lista):
    '''Ordena una lista de elementos según el método de burbujeo.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada.'''
    comparaciones = 0
    n = len(lista)-1
    cambios = True
    while n > 0 and cambios:
        cambios = False
        for i in range (n):
            comparaciones += 1 
            if lista[i] > lista[i+1]:
                p = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = p
                cambios = True
        n -= 1
    return comparaciones


#%%
## ejercicio 12.7
def merge_sort(lista, comparaciones = 0):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
        comparaciones += 1
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio], comparaciones = comparaciones)[0]
        der = merge_sort(lista[medio:], comparaciones = comparaciones)[0]
        m = merge(izq, der)
        lista_nueva = m[0]
        comparaciones += m[1]
    return lista_nueva, comparaciones

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    comparaciones = 0
    while(i < len(lista1) and j < len(lista2)):
        comparaciones += 3
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, comparaciones



#%%
def generar_lista(N):
    ''' genera una lista de largo N con numeros enteros del 1 al 1000
    pre = N debe ser un numero entero positivo
    post = lista con N elementos entre el 1 y el 1000 con posibilidad de repetidos
    '''
    
    lista = [random.randint(1,1000) for i in range(N)]
    return lista

def comparar_metodos (N,k, p = False):
    ''' devuelve el promedio de comparaciones realizadas por los metodos de 
    ordenamiento burbujeo , selección e inserción en una lista de largo N
    k veces
    pre: N y K deben ser enteros positivos
    post: de manera optativa imprime los promedios para cada método si p =True. devuelve una tupla con los promedios 
    en el orden burbuje , seleccion, inserción.
    '''
    comp_burbujeo = 0
    comp_seleccion = 0
    comp_insercion = 0
    comp_ms = 0
    for i in range(k):
        lista = generar_lista(N)
        # variables a ordenar tiene que ser la misma lista para los 3 metodos
        lista_b = lista.copy()
        lista_s = lista.copy()
        lista_i = lista.copy()
        lista_ms = lista.copy()
        # burbujeo
        comp_burbujeo += ord_burbujeo(lista_b)
        #seleccion
        comp_seleccion += ord_seleccion(lista_s)
        #insercion
        comp_insercion += ord_insercion(lista_i)
        #merge sort
        comp_ms += merge_sort(lista_ms)[1]
        
    media_burbujeo = comp_burbujeo/k
    media_seleccion = comp_seleccion/k
    media_insercion = comp_insercion/k
    media_ms = comp_ms/k
    if p:
        print(f'la media del método burbujeo fue {media_burbujeo}')
        print(f'la media del método seleccion fue {media_seleccion}')
        print(f'la media del método insercion fue {media_insercion}')
        print(f'la media del método merge fue {media_ms}')
    return media_burbujeo, media_seleccion, media_insercion, media_ms
    

comparar_metodos(100,1000, p = True)

x = np.array([N for N in range(1,257)])

y_burbujeo = []
y_seleccion = []
y_insercion = []
y_m = []
for N in range(1,257):
    media_metodos = comparar_metodos(N,10) ## aumentando el k, sacando un pormedio por tamaño de lista se puede suavizar
    y_burbujeo.append(media_metodos[0])
    y_seleccion.append(media_metodos[1])
    y_insercion.append(media_metodos[2])
    y_m.append(media_metodos[3])


y_burbujeo = np.array(y_burbujeo)
y_seleccion = np.array(y_seleccion)
y_insercion = np.array(y_insercion)
y_m = np.array(y_m)


plt.plot(y_burbujeo, color = 'red', linestyle = 'dashed', label = 'burbujeo')
plt.plot(y_seleccion, color = 'blue', linestyle = 'dotted', label = 'seleccion')
plt.plot(y_insercion, color = 'green', label = 'insercion')
plt.plot(y_m, color = 'black', label = 'merge')
plt.legend()
plt.show()

# Merge sort es mucho menos costoso que el resto.



lista = generar_lista(20)
