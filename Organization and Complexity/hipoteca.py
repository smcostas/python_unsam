## calculadora de adelantos

print("ejercicio 1.21")
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra = 1000
while saldo > 2684.11:
    if mes >=61 and mes <= 108:
        mes = mes + 1
        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
    else:
        mes = mes + 1
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    print(f'{mes:3} {total_pagado:9.2f} {saldo:9.2f}') 
else:
    mes = mes + 1
    ultimo_pago = abs(saldo * (1+tasa/12))
    saldo = saldo*(1+tasa/12) - ultimo_pago
    total_pagado = total_pagado + ultimo_pago
    print(f'{mes:3} {total_pagado:9.2f} {saldo:9.2f}')    

print(f'se pagará en total {total_pagado:9.2f} en {mes} meses')







