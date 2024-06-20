create database lojinha;
USE lojinha;

create table clientes (
id_cliente int auto_increment not null primary key,
nome varchar(65) not null,
cpf varchar(12) not null
);

create table produtos (
id_produto int auto_increment not null primary key,
nome varchar(50) not null,
preco varchar(4) not null
);

insert into clientes (nome, cpf) values ("Raimundo" , "24761282147");
insert into produtos (nome, preco) values ("Bola" , "50");


select* from clientes;

