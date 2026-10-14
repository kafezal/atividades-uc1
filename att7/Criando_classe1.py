class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

print(type(carro1))
print(type(carro2))