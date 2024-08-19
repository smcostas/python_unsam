# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 12:01:31 2021

@author: Santi
"""

## informe_funciones.py
# 7.5
def leer_precios(direc_precios):
    '''
    usa como parametro la dirección de un archivo csv donde la columna 1 tiene que ser
    los nombres de las frutas y la 2 los precios
    devuelve un diccionario con las frutas como claves  y el precio como valor
    ej precios= {naranja: 15.5, ...}
    '''
    ...
    import fileparse as fp
    with open(direc_precios) as lines:
        precios = dict(fp.parse_csv(lines, types = [str,float], has_headers= False))
    return precios
    ...
    
def leer_camion(direc_camion):
    
    '''
    usa como parametro un la direccion de una tabla csv que contiene los lotes de un camión
    devuelve una lista de disccionarios donde las llaves son el nombre ,cajones y precio y 
    los valores el precio de los mismos 
    ej- camion = [{nombre: Naranaja, cajones: 15, precio: 150}, ...]
    '''
    ...
    import fileparse as fp
    with open(direc_camion) as lines:
        camion = fp.parse_csv(lines, types = [str, int, float] )
    return camion
    ...


def hacer_informe(direc_camion,direc_precios):
    '''
    los parametros son la direccion de una tabla de lotes de un camion
    y la direccion de una tabla de precios
    utiliza las funciones leer_camion y leer_precios para generar
    una lista con el nombre del producto, el numero de cajones, el precio de compre
    y la ganancia.
    '''
    ...
    camion = leer_camion(direc_camion)
    precios = leer_precios(direc_precios)
    valores = []
    for producto in precios:
        for s in camion:
            if producto in s['nombre']:
                dif = precios[producto] - s['precio']
                dato = (s['nombre'], s['cajones'] , s['precio'], dif)
                valores.append(dato)
    return(valores)
    ...
    
def imprimir_informe(informe):
    ...
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    headers =  f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s} ' 
    print(headers)
    print(f'{"-"*10} {"-"*10} {"-"*10} {"-"*10}')
    for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')
    ...
    
def informe_camion(direc_camion,direc_precios):
    ...
    informe = hacer_informe(direc_camion,direc_precios)
    imprimir_informe(informe)
    ...

#informe_camion('../Data/camion2.csv', '../Data/precios.csv')    
#files = ['../Data/camion.csv', '../Data/camion2.csv']   
#for name in files:
#        print(f'{name:-^43s}')
#        informe_camion(name, '../Data/precios.csv')
#        print()
import sys 
def main(argv):
    camion = argv[1]
    precios = argv[2]
    informe_camion(camion,precios)


if __name__ == '__main__':
    main(sys.argv)
    

    
