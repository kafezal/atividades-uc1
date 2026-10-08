#Dados do produto
nome_prod = str(input('digite o nome do produto: '))
preco_prod = float(input('digite o preço do produto: '))
qtd_prod = int(input('digite a quantidade em que vai comprar: '))

#total a pagar
valor = preco_prod * qtd_prod

print(f'o(a) {nome_prod} de preço {preco_prod} reais e de {qtd_prod} unidades')
print(f'você terá que pagar com isso {valor} reais pelo produto')