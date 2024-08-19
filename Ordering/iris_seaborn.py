# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 11:07:56 2021

@author: Santi
"""
import seaborn as sns
from sklearn.datasets import load_iris
iris_dataset = load_iris()

import pandas as pd
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)


# y hacemos una matriz de gráficos de dispersión, asignando colores según la especie
pd.plotting.scatter_matrix(iris_dataframe, c = iris_dataset['target'], figsize = (15, 15), marker = 'o', hist_kwds = {'bins': 20}, s = 60, alpha = 0.8)

#%%

iris_dataframe['target'] = iris_dataset['target']

sns.pairplot(iris_dataframe, hue = 'target', palette="Set3")
