# -*- coding: utf-8 -*-
"""
Created on Mon May 24 13:52:58 2021

@author: Santi
"""
'''
a = [1,9,4,25,16]
i = a.__iter__()
i.__next__()


f = open('../Data/camion.csv')
f.__iter__() 

next(f)
'''
#10.14 versión con expresiones generadoras
class Camion: 
    
    def __init__(self, lotes):
        self.lotes = lotes
    
    def __iter__(self):
        return self.lotes.__iter__()
   
    def __len__(self):
        return len(self.lotes)

    def __getitem__(self, index):
        return self.lotes[index]

    def __contains__(self, nombre):
        return any(lote.nombre == nombre for lote in self.lotes)

    
    def precio_total(self):
        return sum(l.costo() for l in self.lotes)
    
    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for lote in self.lotes:
            cantidad_total[lote.nombre] += lote.cajones
        return cantidad_total
