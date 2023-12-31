							-- Criação das Tabelas
CREATE TABLE aluno (
  id_aluno SERIAL PRIMARY KEY,
  idade INT NOT NULL
  )
  
  CREATE TABLE disciplina (
  id_disciplina SERIAL PRIMARY KEY,
  professor VARCHAR(50) NOT NULL,
  id_aluno INT,  
  CONSTRAINT fk_id_aluno FOREIGN KEY (id_aluno) REFERENCES aluno (id_aluno)
);
							

							-- Inserindo Valores e Atualizando tabela com nova coluna (disciplina.materia)
INSERT INTO aluno (idade, nome_aluno)
VALUES
  (23, 'Joaozinho Silva'),
  (25, 'Maria Santos'),
  (20, 'Pedro Oliveira');
  
ALTER TABLE disciplina 
ADD materia VARCHAR (20) NOT NULL

INSERT INTO disciplina (professor, materia) 
VALUES
	('Marcos', 'Portugues'),
    ('Maria', 'Matematica'),
    ('Ana', 'Artes'),
    ('Fabio', 'Ed. Fisica')
 
INSERT INTO disciplina (professor, materia, id_aluno)
VALUES 
	('Sergio', 'Fisica', 2),
    ('Alessandro', 'Quimica', 2)

							-- Pesquisa utilizando Right Join, retornando o que corresponde da tabela Alunos da tabela disciplina.
SELECT professor, materia, nome_aluno FROM disciplina
RIGHT JOIN aluno
on disciplina.id_aluno = aluno.id_aluno

							-- Nota-se que o resultado é um aluno que não possui disciplina cadastrada retornando "NULL" nos campos de professor e materia.
