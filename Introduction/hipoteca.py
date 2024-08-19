# hipoteca.py
# Ejercicio de hipoteca

## base 1.8
#%%
"""
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
meses = 0
adelanto = 1000
while saldo > 0:
    meses += 1
    if meses <= 12:
        saldo = saldo * (1+tasa/12) - (pago_mensual + adelanto)
        total_pagado = total_pagado + pago_mensual + adelanto
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    
print('Total pagado', round(total_pagado, 2), 'en', meses)
"""
#%%
## 1.9
"""
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
meses = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    meses += 1
    if (meses >= pago_extra_mes_comienzo) and (meses <= pago_extra_mes_fin) : ## uso if para determinar los meses que pago de mas, podría usar otro while
        saldo = saldo * (1+tasa/12) - (pago_mensual + pago_extra)
        total_pagado = total_pagado + pago_mensual + pago_extra
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
        
print('Total pagado', round(total_pagado, 2), 'en', meses)
"""
#%%
## 1.10 y 1.11
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
meses = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    meses += 1
    if pago_mensual <= saldo:
        if (meses >= pago_extra_mes_comienzo) and (meses <= pago_extra_mes_fin) : ## uso if para determinar los meses que pago de mas, podría usar otro while
            saldo = saldo * (1+tasa/12) - (pago_mensual + pago_extra)
            total_pagado = total_pagado + pago_mensual + pago_extra
        else:
            saldo = saldo * (1+tasa/12) - pago_mensual
            total_pagado = total_pagado + pago_mensual
    else: # si es mayor o igual que el saldo
        pago_final = saldo * (1+tasa/12)
        saldo = saldo * (1+tasa/12) - pago_final
        total_pagado = total_pagado + pago_final
        print(f'el pago del ultimo mes fue {pago_final:^.2f}')
    print(f' {meses:^3} {total_pagado:^10.2f} {saldo:^10.2f}')
    
print(f'se pagará en total {total_pagado:9.2f} en {meses} meses')


