CREATE TABLE alunos(
    id INT PRIMARY KEY,
    nome VARCHAR(100)
);

INSERT INTO alunos(id, nome)
VALUES (1, 'Pedro');

SELECT * FROM alunos;

INSERT INTO alunos(id, nome)
VALUES (2, 'Caio');

SELECT * FROM alunos;

SELECT nome FROM alunos WHERE id = 1;

