# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 15:33:05 2021

@author: Santi
"""
#%%
#6.1

def propagar_al_vecino(l):
    modif = False
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1 and l[i+1]==0:
            l[i+1] = 1
            modif = True
        if e==1 and i>0 and l[i-1]==0:
            l[i-1] = 1
            modif = True
    return modif

def propagar(l):
    m = l.copy()
    veces=0
    while propagar_al_vecino(l):
        veces += 1

    print(f"Repetí {veces} veces la función propagar_al_vecino.")
    print(f"Con input {m}")    
    print(f"Y obtuve  {l}")
    return m
#%%
propagar([0,0,0,0,0])
propagar([0,0,1,0,0])
propagar([1,0,0,0,0])
##1 = por que  hay una condicion para esos casos que no tiene que indexar en los bordes (cuando va hacia delante lo tiene que hacer hasta el penultimo valor
## y cuando mira el valor de atras no hacerlo en el primero)
##2 = por que el for corre desde el inicio a hacia la derecha en este caso
## por ende cuando tiene 0 no modifica hasta que encuentre un uno en la derecha o en la izquierda.
## 3 = len(l) - 1 
## 4 = n**2
## 5 = n-1(n**2) veces. es cuadratica.

#%%
## 6.2
def propagar_a_derecha(l):
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1:
            if l[i+1]==0:
                l[i+1] = 1
    return l
#%
def propagar_a_izquierda(l):
    return propagar_a_derecha(l[::-1])[::-1]
#%
def propagar(l):
    ld = l.copy() ## le agrego una copia para que no se modifique la lista original
    ld=propagar_a_derecha(ld)
    lp=propagar_a_izquierda(ld)
    return lp
#%%
l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
print("Estado original:  ",l)
print("Porpagando...")
lp=propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)
# 4 = n-1
# 5 = 3(n-1)
#%%
def trad2s(l):
    '''traduce una lista con 1,0 y -1 
    a una cadena con 'f', 'o' y 'x' '''
    d={1:'f', 0 :'o', -1:'x'}
    s=''.join([d[c] for c in l])
    return s

def trad2l(ps):
    '''traduce cadena con 'f', 'o' y 'x'
    a una lista con 1,0 y -1'''
    inv_d={'f':1, 'o':0, ' x':-1}
    l = [inv_d[c] for c in ps]
    return l

def propagar(l, debug = True):
    s = trad2s(l)
    if debug:
        print(s)#, end = ' -> ')
    W=s.split('')
    PW=[w if ('f' not in w) else 'f'*len(w) for w in W]
    ps=''.join(PW)
    if debug:
        print(ps)
    return trad2l(ps)
#%%
l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
lp = propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)
