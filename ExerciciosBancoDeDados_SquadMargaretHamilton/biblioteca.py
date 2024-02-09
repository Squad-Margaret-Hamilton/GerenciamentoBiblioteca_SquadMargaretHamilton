import sqlite3

biblioteca = sqlite3.connect('biblioteca.bd')
cursor = biblioteca.cursor()

#criacao da tbl
cursor.execute('''
        CREATE TABLE IF NOT EXIST biblioteca (
            id_biblioteca INT PRIMARY KEY, nome VARCHAR (100) NOT NULL,
            telefone INT, nacionalidade VARCHAR (100);')
            ''')

cursor.execute('''
        CREATE TABLE IF NOT EXIST usuarios (
            id_usuario INT PRIMARY KEY, 
            nome VARCHAR (100),telefone INT, 
            endereco VARCHAR (100),nacionalidade VARCHAR (100), 
            email VARCHAR(100), id_biblioteca, FOREIGN KEY(id_biblioteca)
            REFERENCES biblioteca(id_biblioteca);')
               ''')

cursor.execute('''
        CREATE TABLE IF NOT EXIST livros (
            id_livro INT PRIMARY KEY, titulo VARCHAR (100) NOT NULL, 
            editora VARCHAR (100), 
            genero VARCHAR(100), id_biblioteca,id_autor INT, 
            FOREIGN KEY(id_biblioteca) REFERENCES biblioteca(id_biblioteca),
            FOREIGN KEY(id_autor) REFERENCES autor(id_autor);')
            ''')

cursor.execute('''
        CREATE TABLE IF NOT EXIST autores (
            id_autor INT PRIMARY KEY, 
            nome VARCHAR (100),telefone INT,
            genero VARCHAR(100),titulo VARCHAR (100)
            id_biblioteca, FOREIGN KEY(id_biblioteca)
            REFERENCES biblioteca(id_biblioteca)
            ''')

cursor.execute ( '''  
        CREATE TABLE IF NOT EXIST exemplares (
            id_exemplares, data_emprestimo DATE, 
            data_devolucao DATE, limite_renovacao INT,
            estado_exemplar VARCHAR(100),
            id_usuario, id_livro, id_biblioteca,
            FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
            FOREIGN KEY(id_livro) REFERENCES livro(id_livro)
            FOREIGN KEY(id_biblioteca) REFERENCES biblioteca(id_biblioteca);')
            ''')


# # #Inserção de Dados na tabela usuario:

cursor.execute('''
        INSERT INTO biblioteca (id_biblioteca, nome, telefone ,nacionalidade) VALUES 
            (1000 "Marcella Amazonas", 81999999999, "brasileira"),
            (1001, "Priscila Nakayama", 11999999999, "brasileira"),
            (1002, "Pedro Silva", 84999999999, "brasileiro"),
            (1003, "Livia Maria", 91999999999, "brasileira"),
            (1004, "Ana Oliveira", 21999999999, "brasileira"),
            (1005, "Pedro Costa", 22999999999, "brasileiro"),
            (1006, "Laura Fernandes", 33999999999, "brasileira")')
            (1007, "Victor Correia", 54999999999, "brasileiro")')
            (1008, "Eliane Santos", 89999999999, "brasileira")')
            (1009, "Giovana Lacerda", 75999999999, "brasileira")
        ''')

cursor.execute ('''
        INSERT INTO usuarios (id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES
            (1,"Marcella Amazonas", "81999999999", "Avenida Boa Viagem, 545, ap 120, Boa viagem, Recife, Pernambuco", "brasileira", "marcella@gmail.com" ),
            (2,"Priscila Nakayama", "11999999999", "Avenida São Paulo, 234, ap 1200, Mogi das Cruzes, São Paulo", "brasileira", "priscila@gmail.com" ),
            (3,"Pedro Silva", "84999999999", "Rua Professor Luiz, 767, Jaboatão, Recife, Pernambuco", "brasileiro", "pedro@gmail.com" ),
            (4,"Livia Maria", "91999999999", "Rua D, 567, Minas Gerais", "brasileira", "livia@gmail.com" ),
            (5,"Ana Oliveira", "21999999999", "Rua das Graças, 301, Recife, Pernambuco", "brasileira", "ana@gmail.com" ),
            (6,"Pedro Costa", "22999999999", "Travessa F, 123, Salvador, Bahia", "brasileiro", "pedro@gmail.com" ),
            (7,"Laura Fernandes", "33999999999", "Rua das Flores, 5678, Florianópolis, Santa Catarina", "brasileira", "laura@gmail.com" ),
            (8,"Victor Correia", "54999999999", "Rua Guiliano Professor, 9087, ap 2300, João Pessoa,Paraiba", "brasileiro", "victor@gmail.com" ),
            (9,"Eliane Santos", "89999999999", "Avenida dos Ventos, 456, Vista Bela, Piauí", "brasileira", "eliane@gmail.com" ),
            (10,"Giovana Lacerda", "75999999999", "Rua das Borboletas, 123, Jardim Primavera, Alagoas", "brasileira", "giovana@gmail.com" )
             ''')

cursor.execute ('''
        INSERT INTO autores (id_autor, nome, telefone, genero, titulo) VALUES
            (100, "Marcella Amazonas", "81999999999", "romance", "Aventuras na Floresta" ),
            (101, "Priscila Nakayama", "11999999999", "drama", "O Mistério do Castelo" ),
            (102, "Pedro Silva", "84999999999", "suspense", "O Último Desafio" ),
            (103, "Livia Maria", "91999999999", "romance", "Caminhos do Destino" ),
            (104, "Ana Oliveira", "21999999999", "drama", "O Segredo das Estrelas" ),
            (105, "Pedro Costa", "22999999999", "suspense", "Amor em Paris" ),
            (106, "Laura Fernandes", "33999999999", "romance", ""Mistérios do Passado" ),
            (107, "Victor Correia", "54999999999", "suspense", "A Revolta dos Robôs" ),
            (108, "Eliane Santos", "89999999999", "romance", "Pérolas do Oceano" ),
            (109, "Giovana Lacerda", "75999999999", "suspense", "O Navio Pirata")
             ''')
  
cursor.execute('''
        INSERT INTO livro (id_livro, titulo, editora, genero, id_autor, id_biblioteca) VALUES 
        (10 ,"Aventuras na Floresta", "Editora ABC", "romance", 100,1000 )'),
        (11 ,"O Mistério do Castelo", "Editora 123", "drama", 101, 1001 ),
        (12 ,"O Último Desafio", "Editora LivroForte", "suspense", 102,1002 ),
        (13 ,"Caminhos do Destino", "Editora Estelar", "romance", 103,1003 ),
        (14 ,"O Segredo das Estrelas", "Editora Épica", "drama", 104, 1004 ),
        (15 ,"Amor em Paris", "Editora Romântica", suspense, 105,1005 ),
        (16 ,"Mistérios do Passado", "Editora Enigma", "romance", 106,1006 )')
        (17 ,"A Revolta dos Robôs", "Editora Futura", "suspense", 107, 1007)')
        (18 ,"Pérolas do Oceano", "Editora Enigma", "romance", 108, 1008)')
        (19 ,"O Navio Pirata", "Editora Marítima", "suspense", 109,1009 )') 
        ''')


cursor.execute('''
        INSERT INTO exemplares (id_exemplares, data_emprestimo, data_devolucao, limite_renovacao, estado_exemplar, id_usuario, id_livro, id_biblioteca) VALUES
        (1100, "2024-02-06", "2024-03-09", 3, "Emprestado", 1, 10, 1000 ),
        (1200, "2024-02-07", "2024-03-08", 3, "Emprestado", 2, 11, 1001 ),
        (1300, "2024-02-09", "2024-03-11", 3, "Emprestado", 3, 12, 1002 ),
        (1400, "2024-02-10", "2024-03-12", 3, "Emprestado", 4, 13, 1003 ),
        (1500, "2024-02-11", "2024-03-13", 3, "Emprestado", 5, 14, 1004 ),
        (1600, "2024-02-12", "2024-03-14", 3, "Emprestado", 6, 15, 1005 ),
        (1700, "2024-02-13", "2024-03-15", 3, "Emprestado", 7, 16, 1006 ),
        (1800, "2024-02-14", "2024-03-16", 3, "Emprestado", 8, 17, 1007 ),
        (1900, "2024-02-15", "2024-03-17", 3, "Emprestado", 9, 18, 1008 ),
        (2000, "2024-02-16", "2024-03-18", 3, "Emprestado", 10, 19, 1009 )'
            ''')


#Alteracoes na tabela biblioteca

cursor.execute('UPDATE biblioteca SET nacionalidade="uruguaio" WHERE id_usuario=6')
cursor.execute('UPDATE biblioteca SET telefone=87964999990 WHERE nome="Giovana Lacerda"')

##Alteracoes na tabela exemplares
cursor.execute('UPDATE exemplares SET estado_exemplar="Devolvido" WHERE id_livro=1')
cursor.execute('UPDATE exemplares SET data_devolucao="2024-04-05" WHERE id_usuario=2')
cursor.execute('UPDATE exemplares SET estado_exemplar="Atrasado" WHERE data_devolucao > "2024-04-06"')

cursor.execute('UPDATE exemplares SET data_devolucao="2024-03-06" WHERE id_usuario=3')
cursor.execute('UPDATE exemplares SET estado_exemplar="Devolvido" WHERE data_devolucao > "2024-03-06"')

##Alteracoes na tabela livro

cursor.execute('UPDATE livro SET genero="Romance/Ficção" WHERE genero="Romance"')
cursor.execute('UPDATE livro SET autor="Isabela Castro" WHERE autor="Isabela Castr"')

##Alteracoes na tabela usuario
cursor.execute('DELETE FROM usuario WHERE id_usuario=9')
cursor.execute('UPDATE usuario SET nome="Pedro Silva dos Santos" WHERE nome="Pedro Silva"')

##Listar todos os livros disponiveis 
cursor.execute('''SELECT * FROM Livros WHERE id_usuario == Null ''')

##Listar os livros emprestados 
cursor.execute('''SELECT * FROM Livros WHERE id_usuario != Null ''')

##Localizar os livros de um genero 
cursor.execute(''' SELECT * FROM Livros WHERE genero = "romance" ''')

## Verificar o numero de livros de um genero
cursor.execute (''' SELECT especie, COUNT(*) AS disponivel FROM Livros WHERE genero = "romance" ''')

##Escreva consultas SQL para atualizar e excluir registros do banco de dados

cursor.execute('''UPDATE livro SET titulo="Aventuras na Floresta" WHERE id_livro=10''')

##por exemplo, para remover um livro
cursor.execute('''DELETE FROM livro WHERE id_livro=10''')


biblioteca.commit()

biblioteca.close
