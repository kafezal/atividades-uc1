compras = []

for i in range(5):
    compra = input('digite o prouto em compra: ')
    compras.append(compra)

print('=' * 8, 'lista de compras', '=' * 8)
print('Primeiro produto: ', compras[0])
print('Segundo produto: ', compras[1])
print('Terceiro produto: ', compras[2])
print('Quarto produto: ', compras[3])
print('Quinto produto: ', compras[4])