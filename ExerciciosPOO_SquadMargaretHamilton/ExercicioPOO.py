from datetime import datetime, timedelta

class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

class Livro:
    def __init__(self, titulo, editora, generos, renovacoes):
        self.titulo = titulo
        self.editora = editora
        self.generos = generos
        self.renovacoes = renovacoes
        self.autores = []

    def adicionar_autor(self, autor):
        self.autores.append(autor)

class Exemplar:
    def __init__(self, livro):
        self.livro = livro
        self.disponivel = True
        self.data_emprestimo = None
        self.data_devolucao = None
        self.renovacoes_restantes = livro.renovacoes

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            self.data_emprestimo = datetime.now()
            self.data_devolucao = self.data_emprestimo + timedelta(days=7)  # digamos que o emprestimo seja de 7 dias, não sei se precisa dessa informação
            return True
        else:
            return False

def renovar(self):
        if self.renovacoes_restantes > 0:
            self.renovacoes_restantes -= 1
            self.data_devolucao += timedelta(days=7)  # simulando que pode renovar por mais 7 dias, não sei se precisa dessa informação
            return True
        else:
            return False

def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return True
        else:
            return False

class Usuario:
    def __init__(self, nome, telefone, nacionalidade):
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.usuarios = []
        self.livros = []
        self.exemplares = []
        self.emprestimos = [] # penso que aqui precisa acrescentar dentro dessa classe o cadastro de livro, emprestimo a renovação e devolução... 
