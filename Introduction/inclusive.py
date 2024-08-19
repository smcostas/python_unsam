# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:54:33 2023

@author: Santi
"""
#%%
frase = input()
frase = frase.lower()
palabras = frase.split()
frase_t = []
for palabra in palabras:
    if ',' not in palabra:
        if 'o' in palabra[-2:]:
            palabra = palabra[:-2] + palabra[-2:].replace('o','e')
    else:
        if 'o' in palabra[-3:]:
            palabra = palabra[:-3] + palabra[-3:].replace('o','e')
    frase_t.append(palabra)
        
        
frase_t = ' '.join(frase_t)
print(frase_t)
#%%
###  código sin la coma
frase = input()
frase = frase.lower()
palabras = frase.split()
frase_t = []

for palabra in palabras:
    if 'o' in palabra[-2:]:
        palabra = palabra[:-2] + palabra[-2:].replace('o','e')
    frase_t.append(palabra)

#%%
# Código armando una cadena directemente
frase = input("coloque aquí­ su frase \n")
palabras = frase.split()
frase_t = ""

for palabra in palabras:
    if "o" in palabra[-2:]:
        frase_t = frase_t + palabra[:-2] + palabra[-2:].replace("o","e") + " "
    else:
        frase_t = frase_t + palabra + " "

print(frase_t)


