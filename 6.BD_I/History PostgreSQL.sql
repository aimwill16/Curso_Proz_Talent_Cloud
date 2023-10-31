--- 31-10-2023 15:31:21
--- PostgreSQL
drop table pessoa;

--- 31-10-2023 15:33:04
--- PostgreSQL
CREATE TABLE aluno(
  id_aluno SERIAL PRIMARY KEY,
  nome VARCHAR (24),
  email VARCHAR (24),
  endereco VARCHAR (50)
  );

--- 31-10-2023 15:34:10
--- PostgreSQL
INSERT INTO aluno(nome, email, endereco) VALUES ('Joao', 'joao@gmail.com', 'Av. Brasil, 255');

--- 31-10-2023 15:34:25
--- PostgreSQL
SELECT * FROM aluno;

