# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:33:51 2021

@author: Santi
"""
## 7.6 - ciclo
def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma = 0
    if hasta >= desde:
        for x in range (desde, hasta+1):
            suma += x
        #suma = sum([x for x in range(desde, hasta+1)])
    return suma
# 7.7 la invariante es la suma elemento 'desde' hasta 'x' y sale del ciclo cuando x es 'hasta'
sumar_enteros(1,4)

def sumar_enteros(desde,hasta):
    suma = 0
    if hasta >= desde:
        suma_0_1desde = (desde-1)*desde/2 # sumatoria de 1 a desde - 1 (todo lo que quiero descartar)
        suma_0_hasta = hasta*(hasta+1)/2  # sumatoria con el rango completo de 1 a hasta
        suma = int(suma_0_hasta - suma_0_1desde) # al rango completo le resto lo que quiero descartar y obtengo la sumatoria de desde hasta
    return suma

sumar_enteros(5,10)


## 7.8
def valor_absoluto(n):
    '''
    devuelve el valor absoluto de un número n
    pre: n tiene que ser un número (entero o float)
    pos: devuelve el valor absoluto
    inv: no hay invariante.
    '''
    if n >= 0:
        return n
    else:
        return -n

valor_absoluto(32)
def suma_pares(l):
    '''
    la funcion suma los elementos de la lista siempre y cuando estos sean pares
    pre: l tiene que ser una lista con numéros enteros
    pos: devuelve la sumatoria de los numeros pares que esten en la lista. 
        Si la lsita está vacía devuelve 0, si no hay elementos pares devuelve 0
    inv: es la sumatoria de elementos pares en la lista hasta el elemento 'e' de la lista.
        El ciclo termina cuando e es el ultimo elemento en la lista.
    
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res


def veces(a, b):
    '''
    la función devuelve la multiplicación de a por b (suma a, tantas veces como b)
    pre = b tiene que ser un numero entero positivo, a tiene que ser un número (int o float)
    pos = devuelve la multiplicación de a por b
    inv = res = a*(b-nb)
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
veces(2,2.5)

def collatz(n):
    '''
    devuelve la cantidad de pasos necesrios para que un numero n llegue a 1
    mediante la conjetura de Collatz
    pre = n debe ser un entero positivo
    pos = devuelve la cantidad de pasos para que n llegue a 1 mediante Collatz
    inv = 
    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res

        