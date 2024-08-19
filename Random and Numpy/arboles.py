# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 12:29:33 2021

@author: Santi
"""

'''
def leer_arboles(nombre_archivo):
    import csv
    with open(nombre_archivo, 'rt', encoding= 'utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        arbolado=[]
        for row in rows:
            lote=dict(zip(headers, row))
            lote['altura_tot']=float(lote['altura_tot'])
            lote['inclinacio']=int(lote['inclinacio'])
            arbolado.append(lote)
    return arbolado

arboleda = leer_arboles('../Data/arbolado.csv')
H=[float(arbol['altura_tot']) for arbol in arboleda]
print(H)
#%%
## 4.19
jac = [ float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] in {'Jacarandá'} ]
sum(jac)/len(jac)
jac2 =  [ (float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] in {'Jacarandá'} ]
jac2
#%%
## 4.20
def medidas_de_especies(especies,arboleda):
    claves = especies
    dic = {clave:[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] in {clave}] for clave in claves}

    return dic

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
dic = medidas_de_especies(especies,arboleda)
dic
'''

#%%
## 5.24
import matplotlib.pyplot as plt
def leer_arboles(nombre_archivo):
    import csv
    with open(nombre_archivo, 'rt', encoding= 'utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        arbolado=[]
        for row in rows:
            lote=dict(zip(headers, row))
            lote['altura_tot']=float(lote['altura_tot'])
            lote['inclinacio']=int(lote['inclinacio'])
            arbolado.append(lote)
    return arbolado
arboleda = leer_arboles('../Data/arbolado.csv')
altos = [ float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] in {'Jacarandá'} ]

plt.hist(altos,bins=50)
#%%
##5.25
import numpy as np
a = np.array([ float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] in {'Jacarandá'} ])
d = np.array([ float(arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] in {'Jacarandá'} ])
plt.scatter(d,a, c= 'red', alpha = 0.2) ## alpha le da transparencia a los puntos, se puede observar mayor densidad cuando el color es más fuerte ya que se superpone
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")

#%%
## 5.26
def medidas_de_especies(especies,arboleda):
    claves = especies
    dic = {clave:[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] in {clave}] for clave in claves}

    return dic

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
dic = medidas_de_especies(especies,arboleda)
j = np.array(dic['Jacarandá'])
j
e = np.array(dic['Eucalipto'])
p = np.array(dic['Palo borracho rosado'])
jd = j[:,1]
ja = j[:,0]
ed = e[:,1]
ea = e[:,0]
pd = p[:,1]
pa = p[:,0]
plt.scatter(jd,ja, c= 'red', alpha = 0.2) ## alpha le da transparencia a los puntos, se puede observar mayor densidad cuando el color es más fuerte ya que se superpone
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")

plt.scatter(ed,ea, c= 'blue', alpha = 0.2) ## alpha le da transparencia a los puntos, se puede observar mayor densidad cuando el color es más fuerte ya que se superpone
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Eucaliptos")

plt.scatter(pd,pa, c= 'green', alpha = 0.2) ## alpha le da transparencia a los puntos, se puede observar mayor densidad cuando el color es más fuerte ya que se superpone
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Palo borracho")

print(f'la relación es lineal en las 3 especies pero cambia la pendiente (sobre todo en eucaliptos')
def scatter_especies_junto(especies, arboleda):
    'Genera un scatter plot de altura vs diámetro de varias especies'
    medidas = medidas_de_especies(especies, arboleda) # armo las medidas
    colors= ['blue', 'green', 'red']
    i=0
    for especie in especies:
        med= np.array(medidas[especie]) # creo el array
        plt.scatter(med[0:,1], med[0:,0], s= 15, color=colors[i], alpha=0.5)
        plt.xlabel("diametro (cm)")
        plt.ylabel("alto (m)")
        plt.title(f'Relación diámetro-alto para {especies}')
        plt.xlim(0,350) 
        plt.ylim(0,55)
        i += 1
    plt.legend()    
    return plt.show()

scatter_especies_junto(['Eucalipto', 'Palo borracho rosado', 'Jacarandá'], arboleda)
## me faltan las leyendas que no lo logre