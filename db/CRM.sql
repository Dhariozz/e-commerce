create database CRM;
USE CRM;

CREATE TABLE Clientes (
  id_cliente int primary key auto_increment,
    nome VARCHAR(100) not null,
    cpf VARCHAR(12) not null,
    email VARCHAR(100)
);

select * from Clientes;