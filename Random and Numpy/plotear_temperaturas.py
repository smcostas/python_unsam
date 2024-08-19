# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:51:01 2021

@author: Santi
"""

## 5.8
import matplotlib.pyplot as plt
import numpy as np
temperaturas = np.load('../Data/temperatura.npy')
plt.hist(temperaturas,bins=15)
