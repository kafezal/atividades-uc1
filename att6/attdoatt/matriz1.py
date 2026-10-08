# att 1
'''matriz = [
    [10, 20, 30],
    [40, 50, 60],e
    [70, 80, 90]
]

print('primeira linha, segunda coluna: ', matriz[0][1])
print('segunda linha, terceira coluna: ', matriz[1][2])
print('terceira linha, primeira coluna: ', matriz[2][0])'''

# att 2 
'''matriz = [
    [8, 5, 3],
    [2, 7, 9],
    [4, 6, 1]
]

for linha in matriz:
    for numero in linha:
        print(numero)


for linha in matriz:
    print(linha)

for i in matriz:
    for j in i:
        if j % 2 == 0:
            print('número par: ', j)

for linha in matriz:
    for numero in linha:
        if numero > 5:
            print('números maiores que cinco: ', numero)'''

# att3 
'''matriz = [
    [7 ,8, 9],
    [5, 6, 7],
    [8, 9, 10]
]

soma = 0
media = 0

for i in matriz:
    for j in i:
        soma += j
        media += 1
else:
    media = soma / media

print('a soma de tudo deu: ', soma)
print('média da matriz: ', media)

maior = matriz[0][0]
menor = matriz[0][0]

for i in matriz:
    for j in i:
        if j > maior:
            maior = j
        elif j < menor:
            menor = j

print('maior valor: ', maior)
print('menor valor: ', menor)'''

# att 4
'''matriz = []

for i in range(2):
    linha = []

    for j in range(3):
        numero = int(input('digite um número: '))
        linha.append(numero)

    matriz.append(linha)

for linha in matriz:
    print(linha)'''

# att 5 
'''matriz = []

for i in range(3):
    linha = []

    for j in range(3):
        nota = float(input('digite a nota: '))
        linha.append(nota)

    matriz.append(linha)

for i in matriz:
    print(i)

for i in range(3):
    print(f'média do {i + 1} aluno: ', sum(matriz[i]) / len(matriz[i]))'''

# att 6
'''assentos = [
    [0, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1]
]

disp = 0
indisp = 0

for i in assentos:
    for j in i:
        if j == 1:
            disp += 1
        else:
            indisp += 1
    

print('quantidade de assentos disponiveis: ', disp)
print('quantidade de assentos indisponiveis: ', indisp)

for linha in assentos:
    print(linha)

linha_assentos = int(input('digite a fileira do assento: '))
coluna_assentos = int(input('digite a coluna da fileira: '))

if assentos[linha_assentos - 1][coluna_assentos - 1] == 0:
    print('está cadeira está disponivel!!')
else:
    print('este assento está indisponivel!!')'''

# att 7 

matriz_notas = []

for i in range(5):
    aluno = []

    for j in range(3):
        notas = float(input(f'digite a {j + 1} nota do {i + 1} aluno: '))
        aluno.append(notas)

    matriz_notas.append(aluno)

painel_geral = []

for i in len(matriz_notas):
    aluno = []

    media = sum(matriz_notas[i]) / len(matriz_notas[i])
    aluno.append(media)

    if media > 7:
        condicao = 'aprovado'
    elif media >= 5:
        codicao = 'recuperação'
    else:
        condicao = 'reprovado'
    aluno.append(condicao)

    print(f'aluno {i + 1}; média: {media}; condição: {condicao}')