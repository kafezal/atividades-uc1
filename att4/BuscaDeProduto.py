produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Headset']

produto = input('Digite o produto que busca: ')

if produto in produtos:
    print('Produto encontrado')
else:
    print('Produto não achado')