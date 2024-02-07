#criação das tabelas
CREATE TABLE usuario(id_usuario INT PRIMARY KEY, nome VARCHAR (100),telefone INT, endereco VARCHAR (100),nacionalidade VARCHAR (100), email VARCHAR(100));
CREATE TABLE livro(id_livro INT PRIMARY KEY, titulo VARCHAR (100), editora VARCHAR (100), autor VARCHAR(100), genero VARCHAR(100));;
CREATE TABLE biblioteca(id_usuario INT, id_livro INT, nome VARCHAR (100),telefone INT, nacionalidade VARCHAR (100), FOREIGN KEY (id_livro) REFERENCES livro(id_livro),FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario));
CREATE TABLE exemplares(id_usuario INT, id_livro INT, data_emprestimo DATE, data_devolucao DATE, limite_renovacao INT, estado_exemplar VARCHAR(100),FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario), FOREIGN KEY(id_livro) REFERENCES livro(id_livro));

#Inserção de dados tabela usuário
INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (1,"Marcella Amazonas", "81999999999", "Avenida Boa Viagem, 545, ap 120, Boa viagem, Recife, Pernambuco", "brasileira", "marcella@gmail.com" );

INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (2,"Priscila Nakayama", "11999999999", "Avenida São Paulo, 234, ap 1200, Mogi das Cruzes, São Paulo", "brasileira", "priscila@gmail.com" );

INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (3,"Pedro Silva", "84999999999", "Rua Professor Luiz, 767, Jaboatão, Recife, Pernambuco", "brasileiro", "pedro@gmail.com" );

INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (4,"Livia Maria", "91999999999", "Rua D, 567, Minas Gerais", "brasileira", "livia@gmail.com" );

INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (5,"Ana Oliveira", "21999999999", "Rua das Graças, 301, Recife, Pernambuco", "brasileira", "ana@gmail.com" );

INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (6,"Pedro Costa", "22999999999", "Travessa F, 123, Salvador, Bahia", "brasileiro", "pedro@gmail.com" );

INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (7,"Laura Fernandes", "33999999999", "Rua das Flores, 5678, Florianópolis, Santa Catarina", "brasileira", "laura@gmail.com" );

INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (8,"Victor Correia", "54999999999", "Rua Guiliano Professor, 9087, ap 2300, João Pessoa,Paraiba", "brasileiro", "victor@gmail.com" );

INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (9,"Eliane Santos", "89999999999", "Avenida dos Ventos, 456, Vista Bela, Piauí", "brasileira", "eliane@gmail.com" );

INSERT INTO usuario(id_usuario, nome, telefone ,endereco, nacionalidade, email) VALUES (10,"Giovana Lacerda", "75999999999", "Rua das Borboletas, 123, Jardim Primavera, Alagoas", "brasileira", "giovana@gmail.com" );

#Inserção de dados tabela livro
INSERT INTO livro(id_livro, titulo, editora, autor, genero) VALUES (1 ,"Aventuras na Floresta", "Editora ABC", "Carlos Silva", "Aventura" );

INSERT INTO livro(id_livro, titulo, editora, autor, genero) VALUES (2 ,"O Mistério do Castelo", "Editora 123", "Ana Oliveira", "Mistério" );

INSERT INTO livro(id_livro, titulo, editora, autor, genero) VALUES (3 ,"O Último Desafio", "Editora LivroForte", "Pedro Costa", "Ação" );

INSERT INTO livro(id_livro, titulo, editora, autor, genero) VALUES (4 ,"Caminhos do Destino", "Editora Estelar", "Lucas Mendes", "Romance" );

INSERT INTO livro(id_livro, titulo, editora, autor, genero) VALUES (5 ,"O Segredo das Estrelas", "Editora Épica", "Mariana Santos", "Ficção Científica" );

INSERT INTO livro(id_livro, titulo, editora, autor, genero) VALUES (6 ,"Amor em Paris", "Editora Romântica", "Gabriel Oliveira", "Romance" );

INSERT INTO livro(id_livro, titulo, editora, autor, genero) VALUES (7 ,"Mistérios do Passado", "Editora Enigma", "Sophia Lima", "Mistério" );

INSERT INTO livro(id_livro, titulo, editora, autor, genero) VALUES (8 ,"A Revolta dos Robôs", "Editora Futura", "Victor Luiz", "Ficção Científica" );

INSERT INTO livro(id_livro, titulo, editora, autor, genero) VALUES (9 ,"Pérolas do Oceano", "Editora Enigma", "João Rodrigues", "Aventura" );

INSERT INTO livro(id_livro, titulo, editora, autor, genero) VALUES (10 ,"O Navio Pirata", "Editora Marítima", "Isabela Castr", "Aventura" );

#Inserção de dados tabela biblioteca
INSERT INTO biblioteca(id_usuario, id_livro, nome, telefone, nacionalidade) VALUES (1, 1, "Marcella Amazonas", 81999999999, "brasileira");

INSERT INTO biblioteca(id_usuario, id_livro, nome, telefone, nacionalidade) VALUES (2, 2, "Priscila Nakayama", 11999999999, "brasileira");

INSERT INTO biblioteca(id_usuario, id_livro, nome, telefone, nacionalidade) VALUES (3, 3, "Pedro Silva", 84999999999, "brasileiro");

INSERT INTO biblioteca(id_usuario, id_livro, nome, telefone, nacionalidade) VALUES (4, 4, "Livia Maria", 91999999999, "brasileira");

INSERT INTO biblioteca(id_usuario, id_livro, nome, telefone, nacionalidade) VALUES (5, 5, "Ana Oliveira", 21999999999, "brasileira");

INSERT INTO biblioteca(id_usuario, id_livro, nome, telefone, nacionalidade) VALUES (6, 6, "Pedro Costa", 22999999999, "brasileiro");

INSERT INTO biblioteca(id_usuario, id_livro, nome, telefone, nacionalidade) VALUES (7, 7, "Laura Fernandes", 33999999999, "brasileira");

INSERT INTO biblioteca(id_usuario, id_livro, nome, telefone, nacionalidade) VALUES (8, 8, "Victor Correia", 54999999999, "brasileiro");

INSERT INTO biblioteca(id_usuario, id_livro, nome, telefone, nacionalidade) VALUES (9, 9, "Eliane Santos", 89999999999, "brasileira");

INSERT INTO biblioteca(id_usuario, id_livro, nome, telefone, nacionalidade) VALUES (10, 10, "Giovana Lacerda", 75999999999, "brasileira");

#Inserção de dados tabela exemplares
INSERT INTO exemplares(id_usuario, id_livro, data_emprestimo, data_devolucao, limite_renovacao, estado_exemplar) VALUES (1, 1, "2024-01-06", "2024-03-06", 3, "Disponível");

INSERT INTO exemplares(id_usuario, id_livro, data_emprestimo, data_devolucao, limite_renovacao, estado_exemplar) VALUES (2, 2, "2024-01-12", "2024-03-06", 3, "Disponível");

INSERT INTO exemplares(id_usuario, id_livro, data_emprestimo, data_devolucao, limite_renovacao, estado_exemplar) VALUES (3, 3, "2024-02-06", "2024-03-06", 3, "Emprestado");

INSERT INTO exemplares(id_usuario, id_livro, data_emprestimo, data_devolucao, limite_renovacao, estado_exemplar) VALUES (4, 4, "2024-02-06", "2024-03-06", 3, "Emprestado");

INSERT INTO exemplares(id_usuario, id_livro, data_emprestimo, data_devolucao, limite_renovacao, estado_exemplar) VALUES (5, 5, "2024-02-06", "2024-03-06", 3, "Emprestado");

INSERT INTO exemplares(id_usuario, id_livro, data_emprestimo, data_devolucao, limite_renovacao, estado_exemplar) VALUES (6, 6, "2024-02-06", "2024-03-06", 3, "Emprestado");

INSERT INTO exemplares(id_usuario, id_livro, data_emprestimo, data_devolucao, limite_renovacao, estado_exemplar) VALUES (7, 7, "2024-02-06", "2024-03-06", 3, "Emprestado");

INSERT INTO exemplares(id_usuario, id_livro, data_emprestimo, data_devolucao, limite_renovacao, estado_exemplar) VALUES (8, 8, "2024-02-06", "2024-03-06", 3, "Emprestado");

INSERT INTO exemplares(id_usuario, id_livro, data_emprestimo, data_devolucao, limite_renovacao, estado_exemplar) VALUES (9, 9, "2024-02-06", "2024-03-06", 3, "Emprestado");

INSERT INTO exemplares(id_usuario, id_livro, data_emprestimo, data_devolucao, limite_renovacao, estado_exemplar) VALUES (10, 10, "2024-02-06", "2024-03-06", 3, "Emprestado");

#Listar todos os livros disponiveis
SELECT livro.id_livro, livro.titulo, livro.editora, livro.autor, livro.genero
FROM livro
LEFT JOIN exemplares ON livro.id_livro = exemplares.id_livro
WHERE exemplares.estado_exemplar IS NULL OR exemplares.estado_exemplar = 'Disponível';

#Encontrar todos os livros emprestados no momento
SELECT livro.id_livro, livro.titulo, livro.editora, livro.autor, livro.genero
FROM livro
INNER JOIN exemplares ON livro.id_livro = exemplares.id_livro
WHERE exemplares.estado_exemplar = 'Emprestado';

#Localizar os livros escritos por um autor especifico
SELECT *
FROM livro
WHERE autor = 'Carlos Silva';

#Verificar o número de cópias disponivéis de um determinado livro
SELECT COUNT(*)
FROM exemplares
WHERE id_livro = '2' AND estado_exemplar = 'Disponível';

#Mostrar empréstimo em atraso
SELECT *
FROM exemplares
WHERE data_devolucao < DATE('now') AND estado_exemplar = 'Emprestado';