import sqlite3

conexao = sqlite3.connect('biblioteca')
cursor = conexao.cursor()

#criacao da tbl
#cursor.execute('CREATE TABLE usuario(id_usuario INT PRIMARY KEY, nome VARCHAR (100),telefone INT, endereco VARCHAR (100),nacionalidade VARCHAR (100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE livro(id_livro INT PRIMARY KEY, titulo VARCHAR (100), editora VARCHAR (100), autor VARCHAR(100), genero VARCHAR(100));')
#cursor.execute('CREATE TABLE biblioteca(id_usuario INT, id_livro INT, nome VARCHAR (100),telefone INT, nacionalidade VARCHAR (100), FOREIGN KEY (id_livro) REFERENCES livro(id_livro),FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario));')
#cursor.execute('CREATE TABLE exemplares(id_usuario INT, id_livro INT, data_emprestimo DATE, data_devolucao DATE, limite_renovacao INT, estado_exemplar VARCHAR(100),FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario), FOREIGN KEY(id_livro) REFERENCES livro(id_livro));')


#Inserção de Dados:
#cursor.execute('INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (1,"Marcella Amazonas", "81999999999", "Avenida Boa Viagem, 545, ap 120, Boa viagem, Recife, Pernambuco", "brasileira", "marcella@gmail.com" )')
#cursor.execute('INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (2,"Priscila Nakayama", "11999999999", "Avenida São Paulo, 234, ap 1200, Mogi das Cruzes, São Paulo", "brasileira", "priscila@gmail.com" )')
#cursor.execute('INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (3,"Pedro Silva", "84999999999", "Rua Professor Luiz, 767, Jaboatão, Recife, Pernambuco", "brasileiro", "pedro@gmail.com" )')
#cursor.execute('INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (4,"Livia Maria", "91999999999", "Rua D, 567, Minas Gerais", "brasileira", "livia@gmail.com" )')
#cursor.execute('INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (5,"Ana Oliveira", "21999999999", "Rua das Graças, 301, Recife, Pernambuco", "brasileira", "ana@gmail.com" )')
#cursor.execute('INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (6,"Pedro Costa", "22999999999", "Travessa F, 123, Salvador, Bahia", "brasileiro", "pedro@gmail.com" )')
#cursor.execute('INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (7,"Laura Fernandes", "33999999999", "Rua das Flores, 5678, Florianópolis, Santa Catarina", "brasileira", "laura@gmail.com" )')
#cursor.execute('INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (8,"Victor Correia", "54999999999", "Rua Guiliano Professor, 9087, ap 2300, João Pessoa,Paraiba", "brasileiro", "victor@gmail.com" )')
#cursor.execute('INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (9,"Eliane Santos", "89999999999", "Avenida dos Ventos, 456, Vista Bela, Piauí", "brasileira", "eliane@gmail.com" )')
#cursor.execute('INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (10,"Giovana Lacerda", "75999999999", "Rua das Borboletas, 123, Jardim Primavera, Alagoas", "brasileira", "giovana@gmail.com" )')

# cursor.execute('INSERT INTO livros(id_livro, titulo, editora, autor, genero) VALUES (1 ,"Aventuras na Floresta", "Editora ABC", "Carlos Silva", "Aventura" )')
# cursor.execute('INSERT INTO livros(id_livro, titulo, editora, autor, genero) VALUES (2 ,"O Mistério do Castelo", "Editora 123", "Ana Oliveira", "Mistério" )')
# cursor.execute('INSERT INTO livros(id_livro, titulo, editora, autor, genero) VALUES (3 ,"O Último Desafio", "Editora LivroForte", "Pedro Costa", "Ação" )')
# cursor.execute('INSERT INTO livros(id_livro, titulo, editora, autor, genero) VALUES (4 ,"Caminhos do Destino", "Editora Estelar", "Lucas Mendes", "Romance" )')
# cursor.execute('INSERT INTO livros(id_livro, titulo, editora, autor, genero) VALUES (5 ,"O Segredo das Estrelas", "Editora Épica", "Mariana Santos", "Ficção Científica" )')
# cursor.execute('INSERT INTO livros(id_livro, titulo, editora, autor, genero) VALUES (6 ,"Amor em Paris", "Editora Romântica", "Gabriel Oliveira", "Romance" )')
# cursor.execute('INSERT INTO livros(id_livro, titulo, editora, autor, genero) VALUES (7 ,"Mistérios do Passado", "Editora Enigma", "Sophia Lima", "Mistério" )')
# cursor.execute('INSERT INTO livros(id_livro, titulo, editora, autor, genero) VALUES (8 ,"A Revolta dos Robôs", "Editora Futura", "Victor Luiz", "Ficção Científica" )')
# cursor.execute('INSERT INTO livros(id_livro, titulo, editora, autor, genero) VALUES (9 ,"Pérolas do Oceano", "Editora Enigma", "João Rodrigues", "Aventura" )')
# cursor.execute('INSERT INTO livros(id_livro, titulo, editora, autor, genero) VALUES (10 ,"O Navio Pirata", "Editora Marítima", "Isabela Castr", "Aventura" )')

      
      
conexao.commit()
conexao.close
