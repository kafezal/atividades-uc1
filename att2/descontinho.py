prod = float(input('digite o valor do produto: '))

if prod >= 200:
    print(f'o preço {prod} reais vai passar por um desconto de 10%, sendo agora {prod - ((prod * 10) / 100)} reais')

else :
    print(f'você pagará {prod} reais')