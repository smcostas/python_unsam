# -*- coding: utf-8 -*-
"""
Created on Wed May 12 18:21:12 2021

@author: Santi
"""

import pandas as pd
import os

#os.chdir('C:/Users/Santi/Desktop/back up disco/python/program_en_python/Ejercicios/ejercicios_python/Clase08')
df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv')
df.head()
df.index

# usar time como index y que lo lea como timestamp (parse_dates = true)
df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)
df.head()

df['1-18-2014 9:00':'1-18-2014 18:00']
df['2-19-2014']
df['12-25-2014':]

df['12-25-2014':].plot()

df['10-15-2014':'12-15-2014'].plot()

## copia del fragmento 
dh = df['12-25-2014':].copy()
## modifique delta para que el grafico se vea similar
## 8.10
delta_t = -1 # tiempo que tarda la marea entre ambos puertos
delta_h = 17 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()

#%%
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

# Levanto las dos series
df=pd.read_csv('../Data/OBS_SHN_SF-BA.csv',index_col=['Time'],parse_dates=True)
# Me quedo con un fregmento
dh=df['10-01-2014':].copy()

# Selecciono los intervalos que voy a usar para desplazar SF
shifts = np.arange(-12,13)
# Genero un vector donde guardar los coeficientes de correlacion para cada deslpazamiento
corrs = np.zeros(shifts.shape)
for i, sh in enumerate(shifts):
    #guardo el coeficiente de correlación r entre de SF desplazada con BA original.
    corrs[i] = pearsonr(dh['H_SF'].shift(sh)[12:-12],dh['H_BA'][12:-12])[0]
# ploteo los resultados   
plt.plot(shifts, corrs)

#%%

# Cada cuarto de hora
df=pd.read_csv('../Data/OBS_SHN_SF-BA.csv',index_col=['Time'],parse_dates=True)
dh =df['10-01-2014':].copy() #ultimo trimestre
freq_horaria = 60 # 4 para 15min, 60 para 1min
cant_horas = 24
N = cant_horas * freq_horaria
#resampleo cada tantos minutos
dh = dh.resample(f'{int(60/freq_horaria)}T').mean()
#rellenos los NaNs suavemente
dh =dh.interpolate(method='quadratic')
# genero vector de desplazamientos (enteros)
ishifts = np.arange(-N,N+1)
# y su desplamiento horario asociado
shifts=ishifts/freq_horaria
# finalmente calculo las correlaciones correspondientes
corrs = np.zeros(shifts.shape)
for i, sh in enumerate(ishifts):
    corrs[i] = pearsonr(dh['H_SF'].shift(sh)[N:-N],dh['H_BA'][N:-N])[0]
# y grafico
plt.plot(shifts, corrs)
np.argmax(corrs)
desfasaje = shifts[np.argmax(corrs)]
desfasaje = desfasaje*60/1
print(f'el desfasaje es de {abs(desfasaje)} min')
