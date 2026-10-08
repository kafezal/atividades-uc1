# teste 1
'''nomes = ['Ana', 'João', 'Maria', 'Pedro']

print('o nome dos sorteados são: ', nomes)'''

# teste 2
'''frutas = ['Maçã', 'Bana', 'Uva']

frutas[1] = 'Laranja'

print(frutas)'''

# teste 3: ler quantos itens na lista
'''nomes = ['Ana', 'João', 'Maria', 'Pedro']

print(len(nomes))'''

# teste 4: a quantidade de elementos da lista no for
'''nomes = ['Ana', 'João', 'Maria']

for nome in nomes:
    print(nome)'''

# teste 5 a quantidade de elementos da lista no while
'''nomes = ['Ana', 'João', 'Maria']

i = 0

while i < len(nomes):
    print(nomes[i])
    i += 1'''

# teste 6: adicionando na lista
'''nomes = []

nomes.append('Ana')
nomes.append('Carlos')
nomes.append('Maria')

print(nomes)'''

# teste 7
'''notas = []

for i in range(5):
    nota = float(input('digite uma nota: '))
    notas.append(nota)
print(notas)'''

# teste 8
'''nomes = ['Ana', 'Maria']

nomes.insert(1, 'Carlos')

print(nomes)'''

# teste 9
'''nomes = ['Ana', 'Carlos', 'Maria']

nomes.remove('Carlos')

print(nomes)'''

# teste 10

'''nomes = ['Ana', 'Carlos', 'Maria']

nomes.pop(1)

print(nomes)'''

#teste 11
'''nomes = ['Ana', 'Carlos', 'Maria']

nome = input('digite um nome: ')

if nome in nomes :
    print('nome encontrado!')
else:
    print('nome não encontrado')'''

#teste 12
'''notas = [7.5, 8.0, 9.0, 6.5]

media = sum(notas) / len(notas)

print('média: ', media)'''

#teste 13
'''notas = [7.5, 8.0, 9.0, 6.5]

print('maior: ', max(notas))
print('menor: ', min(notas))'''

#teste 14
'''notas = []

for i in range(5):
    nota = float(input('digite a nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)

print('notas: ', notas)
print('maior nota: ', max(notas))
print('menor nota: ', min(notas))
print('média: ', media)'''