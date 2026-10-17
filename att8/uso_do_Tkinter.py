import tkinter as tk

# criando uma janela
janela = tk.Tk()
janela.title("Meu primeiro aplicativo")
janela.geometry("400x300")

# Adicionar um rótulo
rotulo = tk.Label(
    janela,
    text="Cadastro de alunos!",
    font=("Arial", 16)
)

rotulo.pack()

# Entrada dos dados
campo_nome = tk.Entry(janela)
campo_nome.pack()

# obtendo um texto digitado
'''nome = campo_nome.get()
print(nome)'''

campo_nome.delete

# criando um botão q capture os dados
def cadastrar():
    nome = campo_nome.get()
    print("Nome cadastrado: ", nome)

botao = tk.Button(
    janela, 
    text='Cadastrar',
    command=cadastrar
    )
botao.pack()

# executar um loop principal
janela.mainloop()