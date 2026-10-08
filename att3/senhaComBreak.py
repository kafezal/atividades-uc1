for tentativa in range(4):
    senha = str(input('digite a sua senha: '))

    if senha != 'python123':
        print('acesso negado')
        print(f'tente novamente, você tem {3 - tentativa} tentativas para fazer')
    else:
        print('acesso permitido')
        print('-' * 5,' bem vindo ', '-' * 5)
        break
    if tentativa == 3:
        print('fechando programa...')
        break