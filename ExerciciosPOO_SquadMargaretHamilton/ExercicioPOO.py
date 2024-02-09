from datetime import datetime, timedelta


class Pessoa:
    def __init__(self, nome, telefone,nacionalidade):
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade
        self.__data_cadastro = datetime.now()  

class Usuario(Pessoa):
      def __init__(self,nome, telefone, endereco, nacionalidade, email ):
        super(Usuario, self).__init__(
            nome=nome,
            telefone=telefone,
            nacionalidade=nacionalidade,
        )  
        self.endereco = endereco
        self.email = email
    

class Autor(Pessoa):
    def __init__(self, nome, telefone, genero):
        super(Autor, self).__init__(
            nome=nome,
            telefone=telefone,
            nacionalidade=None,
        )
        self.genero = genero

class Livro:
    def __init__(self, titulo, editora, generos, renovacoes, disponibilidade):
        self.titulo = titulo
        self.editora = editora
        self.generos = generos
        self.renovacoes = renovacoes
        self.disponibilidade = disponibilidade
        self.autores = []


        @property
        def disponibilidade(self):
            if self.usuario:
                return False
            return True
        
        def registrar_autor(self,autor_id, nome,telefone, genero,titulo):
            autor = Autor(nome, telefone, genero,titulo)
            self.autor[autor_id] = autor

class Biblioteca:
    def __init__(self, nome, telefone, nacionalidade):
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade
        self.usuarios = {} 
        self.livros = {}
        self.emprestimos = []
        self.renovacoes = []
        
        def registrar_usuario(self,id_usuario, nome,telefone, endereco, nacionalidade, email):
            usuario = Usuario(nome, telefone, endereco, nacionalidade, email)
            self.usuarios[id_usuario] = usuario
        
        def registrar_livro(self,livro_id, titulo, editora, generos, renovacoes, disponibilidade):
            livro = Livro(titulo, editora, generos, renovacoes, disponibilidade)
            self.livros[livro_id] = livro
       
            
        def emprestar_livro(self,livro, usuario,data_emprestimo, data_devolucao, num_renovacao):
            if self.disponivel == True:
             emprestimo = {"livro": livro, "usuario": usuario, "data_emprestimo": data_emprestimo, "data_devolucao": data_devolucao, "num_renovacao": num_renovacao}
             self.data_emprestimo = datetime.now()
             self.data_devolucao = self.data_emprestimo + timedelta(days=7)  # digamos que o emprestimo seja de 7 dias, não sei se precisa dessa informação
             self.emprestimos.append(emprestimo)
    
            else:
             None

        def renovar(self,emprestimo):
            if self.renovacoes_restantes > 0:
                 self.renovacoes_restantes -= 1
                 renovar = {"emprestimo": emprestimo, "renovar": self.data_devolucao}
                 self.data_devolucao += timedelta(days=7)  # simulando que pode renovar por mais 7 dias, não sei se precisa dessa informação
                 self.renovacoes.append(renovar)
            return True
            
        def devolver(self,emprestimo):
            self.emprestimos.remove(emprestimo)

import biblioteca_db 
biblioteca = biblioteca_db.Biblioteca()
obj_bibliotecas = {}

for biblioteca in Biblioteca:
    obj_bibliotecas[biblioteca[0]] = biblioteca(
        nome=biblioteca[1],
        telefone=biblioteca[2],
        nacionalidade=biblioteca[3],
    )


        

            




    