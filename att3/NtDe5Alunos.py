for aluno in range(1, 6):

    print(f'{aluno}° aluno')
    nota = float(input('informe sua nota: '))

    if nota >= 7:
        print(f'{nota} faz você aprovado!')
    elif nota >= 5:
        print(f'{nota} faz você entrar em recuperação')
    else:
        print(f'{nota} faz você ser reprovado')