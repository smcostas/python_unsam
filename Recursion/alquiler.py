# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 11:42:16 2021

@author: Santi
"""
import numpy as np
import matplotlib.pyplot as plt

def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b


superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

ab = ajuste_lineal_simple(superficie, alquiler)
a = ab[0]
b = ab[1]

minx = min(superficie)
maxx = max(superficie)
grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
grilla_y = grilla_x*a + b

g = plt.scatter(x = superficie, y = alquiler)
plt.title('alquileres en función de la superficie en Caballito, CABA')
plt.plot(grilla_x, grilla_y, c = 'red')
plt.xlabel('superficie en m2')
plt.ylabel('alquiler en miles de pesos')
plt.show()

errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())

'''
## relacion cuadratica 

np.random.seed(3141) # semilla para fijar la aleatoriedad
N=50
indep_vars = np.random.uniform(size = N, low = 0, high = 10)
r = np.random.normal(size = N, loc = 0.0, scale = 8.0) # residuos
dep_vars = 2 + 3*indep_vars + 2*indep_vars**2 + r # relación cuadrática

x = indep_vars
y = dep_vars
plt.scatter(x,y)
plt.title('scatterplot de los datos')
plt.show()


a, b = ajuste_lineal_simple(x, y)

grilla_x = np.linspace(start = 0, stop = 10, num = 1000)
grilla_y = grilla_x*a + b
g = plt.scatter(x = x , y = y)
plt.title('ajuste lineal')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.show()

errores = y - (x*a + b)
print("ECM", (errores**2).mean()) ## error cuadratico medio muy grande
'''