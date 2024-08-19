# -*- coding: utf-8 -*-
"""
Created on Fri May 19 12:36:40 2023

@author: Santi
"""

import os
os.chdir('C:/Users/Santi/ejercicios python unsam nuevo/Clase03')


#%%
# ejercicio 3.1

# por un lado no detecta mayuculas (no se si queremos hacerlo) por otro el problema es como esta estructurado el codigo. al terner el return como true or false dentro del bloque if, si la primer letra no es a automaticamente el ciclo for se corta retornando false, y no continua con el resto de las letras.
# solucion a continuacion
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    tiene = False # agrego una variable que por default sea falsa para ser cambiada solo si la palbra tiene la letra a
    while i<n and not tiene:
        if (expresion[i] == 'a') or (expresion[i] == 'A'):
            tiene = True # es cambiada cuando tiene a o A
        i += 1
    return tiene # devuelvo la variable de esta forma controlo que continue por toda la frase

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
# ejercicios 3.2
# en este caso, no esta bien la sintaxis faltan : en la def y en los diferentes ciclos y bloques. también una e y otras cosas
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] =='a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
# 3.3
## no funcionaba cuando se le introducia un numero (entereo en este caso) en lugar de una string
## se puede solucionar convirtiendo la expresione en una string siempre
def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)
tiene_uno(7881.5)

#%%
#3.4
# el problema es que no tiene return
def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
import csv
from pprint import pprint
import os
#os.chdir('ejercicios python unsam nuevo/Clase03')
## el problema es que al no crear un registro cada vez sino sobreescribir la llaves, 
## cada vez que sobre esribo el registro  este es sobreescribe todos los registros del camion
# se soluciona creando un resgistro por cada fila (ya que asi el resgistro solo existe mientras esta en el ciclo    )
def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for i,fila in enumerate(filas):
            registro = {}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

cam = '../Data/camion.csv'
camion = leer_camion(cam)
pprint(camion)
registro = {'cable':15, 'tele':13}
lista = []
lista.append(registro)
lista[0] is registro
registro['cable'] = 13


a = 2
b = a
a is b


a = [1,2,3,4,5]
b = a


b = [1,2,3,4,5]
a == b
