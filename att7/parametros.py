class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

conta1 = Conta('Maria', 100)

conta1.depositar(50)

print(conta1.saldo)
