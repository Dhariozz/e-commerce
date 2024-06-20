import mysql.connector  # conexão entre o vscode e o workbench

class Contato: # criação da classe "contato"
    def __init__(self, nome, contato):  # definindo atributos da classe
        self.nome = nome # atribuindo uma valor a um atributo da classe 
        self.contato = contato # está atribuindo o valor da variável ao atributo
class SistemaDeContatos: # criação da classe sistemadecontatos
    def __init__(self): # está definindo o construtor de uma classe
        self.conexao = mysql.connector.connect( # estabelecendo uma conexão com o banco de dados MySQL
            host="localhost", # está definindo uma variável e atribuindo a ela um valor
            user="root", # está atribuindo um valor a uma variável 
            password="he182555@", # está atribuindo a string  "he18255@" a variável 
            database="contatos_db" # está especificando o nome do banco de dados que será utilizado para fazer a conexão com o banco SGBD 
        )
        self.cursor = self.conexao.cursor() # está criando um cursor para a conexão de banco de em 'self.conexão'

    def adicionar_contato(self, contato): # adicionando contato na tabela contato
        sql = "INSERT INTO contatos (nome, contato) VALUES (%s, %s)" # está fazendo a inserção de dados em uma tabela chamada 'contatos'
        valores = (contato.nome, contato.contato) # está criando uma tupla com dois elementos, o valor da propriedade 'nome' e o valor da propriedade 'contato'
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        print('Contato adicionado com sucesso.')

    def listar_contatos(self): #está definindo uma função listar contatos
        self.cursor.execute("SELECT nome, contato FROM contatos") # ele vai selecionar nome, contato da tabela contato
        contatos = self.cursor.fetchall() # está a recuperar o resultado da consulta 
        for contato in contatos: # o for vai percorrer uma lista chamada contatos e atribuir cada elemento desta lista a variável 'contato'
            print(f"Nome: {contato[0]}, Contato: {contato[1]}") # vai imprimir o nome e o contato armazenados em uma lista chamada 'contato'

    def fechar_conexao(self): # o metódo fechar conexão  está sendo definido dentro de uma classe, indicada pelo self
        self.cursor.close() # está fechando o cursor associado a conexão 
        self.conexao.close() # está encerrando a conexão com o banco de dados

# Istancia o sistema de contatos
sistema = SistemaDeContatos() 

# Cria contatos
contato1 = Contato('Patatibn', "45673233")
contato2 = Contato('Patatavb', "23435678")

#Adiciona contatos
sistema.adicionar_contato(contato1)
sistema.adicionar_contato(contato2)

# Lista contatos
print("Lista de contatos: ")
sistema.listar_contatos()

# Fecha a conexão
sistema.fechar_conexao()




 


     
