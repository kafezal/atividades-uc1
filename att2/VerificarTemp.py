temp = float(input('digite a temperatura: '))

if temp > 30 :
    print(f'{temp} °C é muito quente')

elif temp >= 20 :
    print(f'{temp} °C é agradavel')

elif temp >= 10 :
    print(f'{temp} °C é frio')

else:
    print(f'{temp} °C é muito frio')