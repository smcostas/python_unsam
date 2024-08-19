# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 12:16:18 2021

@author: Santi
"""
import random
temperatura = [random.normalvariate(37.5,0.2) for i in range(99)]
print(temperatura)
maxx = max(temperatura)
minn = min(temperatura)
media = sum(temperatura)/len(temperatura)
temperatura.sort()
mediana = temperatura[int(len(temperatura)/2)]
primercuartil = temperatura[int(len(temperatura)/4)]
tercercuartil = temperatura[int(len(temperatura)*0.75)]
print(f' media   max    min  mediana  1qr    3qr')
print(f'{media:6.2f} {maxx:6.2f} {minn:6.2f} {mediana:6.2f} {primercuartil:6.2f} {tercercuartil:6.2f}')

'''
## 5.7 
import numpy as np
temperaturas = np.array([random.normalvariate(37.5,0.2) for i in range(99)])
temperaturas
np.save('../Data/temperatura.npy', temperaturas)
'''