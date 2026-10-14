class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print('Olá, meu nome é ', self.nome)

aluno1 = Aluno('Ana', 19)
    
aluno1.apresentar()