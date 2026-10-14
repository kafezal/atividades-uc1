class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

aluno1 = Aluno('Ana', 19)
aluno2 = Aluno('Carlos', 22)

print(aluno1.nome)
print(aluno2.nome)