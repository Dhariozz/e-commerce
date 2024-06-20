create database escola_tecnica;
USE escola_tecnica;

create table alunos (
id_aluno int auto_increment not null primary key,
nome varchar(60),
cpf varchar(12)
);
insert into alunos (nome, cpf) values ("josé dhario" , "1132358943");
select* from alunos;
