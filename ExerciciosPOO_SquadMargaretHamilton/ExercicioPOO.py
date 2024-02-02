from datetime import datetime, timedelta

class Usuario:
    def __init__(self, nome, telefone, nacionalidade):
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade

class Autor(Usuario):
    def __init__(self, nome, nacionalidade, telefone, obras):
        super().__init__(nome, telefone, nacionalidade)
        self.obras = obras

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

class Emprestimo:
    def __init__(self, exemplar, usuario):
        self.exemplar = exemplar
        self.usuario = usuario
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None
    
    def devolver(self):
        self.exemplar.devolver()
        self.data_devolucao = datetime.now()

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.usuarios = []
        self.livros = []
        self.exemplares = []
        self.emprestimos = [] # penso que aqui precisa acrescentar dentro dessa classe o cadastro de livro, emprestimo a renovação e devolução... 

    def cadastrar_livro (self, livro):
        self.livros.append(livro)
        self.exemplares.extend([Exemplar(livro) for _ in range (5)])
    
    def realizar_emprestimo(self, exemplar, usuario):
        if exemplar.emprestar():
            emprestimo = Emprestimo(exemplar, usuario)
            self.emprestimos.append(emprestimo)
            return emprestimo
        else:
            return None
    
    def renovacao_emprestimo(self, emprestimo):
        exemplar = emprestimo.exemplar
        if exemplar.renovar():
            return True
        else:
            return False
    
    def devolucao(self, emprestimo):
        emprestimo.devolver()

autor1 = Autor("John Green", "Americano", "123456789", ["Obra1", "Obra2"])
livro1 = Livro("Meu coração e outros buracos negros", "Editora1", ["Ação", "Aventura"], renovacoes=2)
livro1.adicionar_autor(autor1)

usuario1 = Usuario("Laryssa", "987654321", "Brasileira")

biblioteca = Biblioteca("Biblioteca Estadual")
biblioteca.cadastrar_livro(livro1)

exemplar_disponivel = biblioteca.exemplares[0]
emprestimo1 = biblioteca.realizar_emprestimo(exemplar_disponivel, usuario1)

if emprestimo1:
    print(f"Empréstimo realizado em {emprestimo1.data_emprestimo}.")
    print(f"Data de devolução prevista: {emprestimo1.data_devolucao}")

    # Tentativa de renovação
    if biblioteca.renovacao_emprestimo(emprestimo1):
        print("Renovação realizada com sucesso.")
    else:
        print("Não foi possível renovar o empréstimo.")

    # Devolução do exemplar
    biblioteca.devolucao(emprestimo1)
    print(f"Empréstimo devolvido em {emprestimo1.data_devolucao}.")
else:
    print("Não foi possível realizar o empréstimo.")
