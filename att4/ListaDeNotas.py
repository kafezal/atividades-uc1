notas = []

for i in range(5):
    nota = float(input(f'Digite a nota do {i + 1} aluno: '))
    notas.append(nota)

media = sum(notas) / len(notas)

print('Todas as notas: ', notas)
print('A média é: ', media)
print('A maior nota é: ', max(notas))
print('A menor nota é: ', min(notas))