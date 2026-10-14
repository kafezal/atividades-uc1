class Celular:
    def __init__(self, marca, modelo, preco):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco

celular1 = Celular('samsung', 'A11', 1.200)
celular2 = Celular('Motorolla', 'megapower', 2.345)

print('Marca: ', celular1.marca)
print('modelo: ', celular1.modelo)
print('preço: ', celular1.preco)

print('Marca: ', celular2.marca)
print('modelo: ', celular2.modelo)
print('preço: ', celular2.preco)