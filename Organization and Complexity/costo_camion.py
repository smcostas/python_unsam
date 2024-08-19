## ejercicio 2.2
'''
gasto_total = 0
with open('C:/Users/Santi/Desktop/back up disco/python/program_en_python/Ejercicios/ejercicios_python/Data/camion.csv', 'rt') as f:
     headers = next(f)
     for line in f:
         row = line.split(",")
         gasto_cajon = int(row[1])*float(row[2])
         gasto_total += gasto_cajon
         print(f'gasto en cajones de {row[0]} = {gasto_cajon}')
print("\nse gasto en total =",gasto_total)
'''


## ejercicio 2.6
'''
def costo_camion(nombre_archivo):
    ...
    gasto_total = 0
    with open(nombre_archivo, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(",")
            gasto_cajon = int(row[1])*float(row[2])
            gasto_total += gasto_cajon
            print(f'gasto en cajones de {row[0]} = {gasto_cajon}')
    #print("\nse gasto en total =",gasto_total) ## no me interesa printear esto.
    return(gasto_total) ## por si lo quiero usar mas adelante.
    ...

costo = costo_camion('C:/Users/Santi/Desktop/back up disco/python/program_en_python/Ejercicios/ejercicios_python/Data/missing.csv')
print('Costo total:', costo)
'''
## Ejercicio 2.8
'''
def costo_camion(nombre_archivo):
    ...
    gasto_total = 0
    with open(nombre_archivo, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(",")
            try:
                gasto_cajon = int(row[1])*float(row[2])
                gasto_total += gasto_cajon
                print(f'gasto en cajones de {row[0]} = {gasto_cajon}')
            except ValueError:
                print(f'missing values for {row[0]}')
    #print("\nse gasto en total =",gasto_total) ## no me interesa printear esto.
    return(gasto_total) ## por si lo quiero usar mas adelante.
    ...

costo = costo_camion('../Data/missing.csv')
print('Costo total:', costo)
'''
"""
## Ejercicio 2.10
import csv
def costo_camion(nombre_archivo):
    ...
    gasto_total = 0
    with open(nombre_archivo, 'rt') as f:
        next(f)
        for line in f:
            row = line.split(",")
            try:
                gasto_cajon = int(row[1])*float(row[2])
                gasto_total += gasto_cajon
                print(f'gasto en cajones de {row[0]} = {gasto_cajon}')
            except ValueError:
                print(f'missing values for {row[0]}')
    #print("\nse gasto en total =",gasto_total) ## no me interesa printear esto.
    return(gasto_total) ## por si lo quiero usar mas adelante.
    ...
costo = costo_camion('../Data/missing.csv')
print('Costo total:', costo)
"""

def costo_camion(nombre_archivo):
    ...
    from informe_funciones import leer_camion
    camion = leer_camion(nombre_archivo)
    gasto_total = sum([lote['cajones'] * lote['precio'] for lote in camion])
    
    #for lote in camion:
    #    gasto_total += lote['cajones'] * lote['precio']
    #print("\nse gasto en total =",gasto_total) ## no me interesa printear esto.
    
    return gasto_total ## por si lo quiero usar mas adelante.
    ...
costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
