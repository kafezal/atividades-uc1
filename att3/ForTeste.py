# método 1
'''for numeros in range(5):
    print(numeros)'''

# método 2
'''for numeros in range(0, 11, 2):
    print(numeros)'''

# teste próprio
inicio = int(input('digite um número que começa: '))
fim = int(input('digite quando que acaba: '))
periodo = int(input('digite o incremento da contagem: '))

for intervalo in range(inicio, fim + 1, periodo):
    print(intervalo)