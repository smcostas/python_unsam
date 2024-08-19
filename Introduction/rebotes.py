# rebotes.py

# Ejercicio

## mi codigo

#%%
rebote = 0
salto = 3/5
alt = 100

while  rebote < 10:
    rebote += 1
    alt = alt*salto
    print(rebote, round(alt, 2))
    
#%%    
## ayuda a ro 
altura_inicial = 100
rebotes = 10
rebote = 0
while rebotes > 0:
    altura_caida = altura_inicial * 3/5
    rebote +=1
    print(rebote, round(altura_caida,2))
    altura_inicial *= 3/5
    rebotes -= 1
#%%
# otra forma con ciclo for
alt = 100
salto = 3/5      
 
for rebote in range(10):
    rebotes = rebote + 1
    alt = alt*salto
    print(rebotes, round(alt, 2))


