# -*- coding: utf-8 -*-
"""
Created on Mon May 10 20:36:09 2021

@author: Santi
"""
#%%
#8.2
import datetime

def cuanto_falta_primavera():
    ''' arroja cuantos días falta para la primavera'''
    date_today = datetime.date.today()
    primavera = datetime.date(year = 2021, month = 9, day = 21)
    delta_dias = primavera - date_today
    
    print (f'faltan {delta_dias.days} días para la primavera')

cuanto_falta_primavera()

#%%
#8.3
import datetime
licencia = datetime.timedelta(days = 200)
inicio = datetime.datetime(year = 2020, month = 9, day = 26)
fin = inicio + licencia
print(f'luego de la licencia la reincorporación es el {fin}')

#%%
#8.4
import datetime
def dias_habiles(inicio,fin,feriados = []):
    ...
    if inicio >= fin:
        raise 'la fecha inicial debe ser menor a la inicial'
    lista_feriados = [datetime.datetime.strptime(feriados[i], '%d/%m/%Y') 
                      for i in range(len(feriados))]
    date_inicial = datetime.datetime.strptime(inicio, '%d/%m/%Y')
    date_final = datetime.datetime.strptime(fin, '%d/%m/%Y')
    dia = datetime.timedelta(days = 1)
    habiles = []
    while date_inicial <= date_final:
        if date_inicial not in lista_feriados:
            sdate = date_inicial.strftime('%d/%m/%Y')
            habiles.append(sdate)
            date_inicial += dia
        else:
            date_inicial += dia
    return habiles

inicio = '20/09/2020'
fin = '10/10/2020'
habiles = dias_habiles(inicio,fin)
print(habiles)

feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']
inicio = '10/10/2020'
fin = '31/12/2020'

habiles = dias_habiles(inicio,fin, feriados)
print(habiles)
