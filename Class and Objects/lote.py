# -*- coding: utf-8 -*-
"""
Created on Wed May 19 10:22:15 2021

@author: Santi
"""

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    
    def costo(self):
        return self.cajones * self.precio
    
    def vender(self, n):
        self.cajones -= n   
        
    