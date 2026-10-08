#teste 1
'''matriz = [
    [5, 8, 2],
    [7, 3, 9],
    [4, 6, 1]
]

print(matriz[1][2])'''

# teste 2
'''matriz = [
     [10, 20],
     [30, 40]
]
print(matriz)'''

# teste 3
'''matriz = [
    [10, 20],
    [30, 40]
]
matriz[0][1] = 99

print(matriz)'''

# teste 4
'''matriz = [
    [10, 20, 30],
    [40, 50, 60]
]

# for numero in matriz[0]:
    # print(numero)

for linha in matriz:
    for numero in linha:
        print(numero)'''

# teste 5
'''matriz = [
    [10, 20, 30],
    [40, 50, 60]
]

# o i de linha
# o j de coluna
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print('linha: ', i)
        print('coluna: ', j)
        print('valor: ', matriz[i][j])'''
# teste 6
'''matriz = []

for i in range(3):
    linha = []

    for j in range(3):
        numero = int(input('digite um número: '))
        linha.append(numero)
    matriz.append(linha)

for linha in matriz:
    print(linha)

    soma = 0

for linha in matriz:
    for numero in linha:
        soma += numero

print('soma: ', soma)

for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            print(numero)

quantidade = 0

for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            quantidade += 1

print('quantidade de números pares: ', quantidade)'''

# teste 7
'''matriz = []

for i in range(3):
    linha = []

    for j in range(3):
        numero = int(input('digite um número: '))
        linha.append(numero)
    matriz.append(linha)

maior = matriz[0][0]

for linha in matriz:
    for numero in linha:
        if numero > maior:
            maior = numero
print('maior: ', maior)'''

# teste 8
'''matriz = []

for i in range(3):
    linha = []

    for j in range(3):
        numero = int(input('digite um número: '))
        linha.append(numero)
    matriz.append(linha)

soma = 0

for numero in matriz[0]:
    soma += numero

print('a soma da primeira linha: ', soma)'''

# teste 9
matriz = []

for i in range(3):
    linha = []

    for j in range(3):
        numero = int(input('digite um número: '))
        linha.append(numero)
    matriz.append(linha)

soma = 0

for linha in matriz:
    soma = soma + linha[1]

for linha in matriz:
    print(linha)

print('soma da coluna: ', soma)

# resposta do teste 9
atriz = []

for i in range(3):
    linha = []

    for j in range(3):
        numero = int(input('digite um número: '))
        linha.append(numero)
    matriz.append(linha)

soma = 0

for i in range(len(matriz)):
    soma += matriz[i][0]

print('a soma da primeira coluna: ', soma)