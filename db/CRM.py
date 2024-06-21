import mysql.connector

class Cliente:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

class SistemaDeRegistros:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="he182555@",
            database="CRM"
        )
        self.cursor = self.conexao.cursor()

    def registrar_cliente(self, cliente):
        sql = "INSERT INTO clientes (nome, cpf, email) VALUES (%s, %s, %s)"
        valores = (cliente.nome, cliente.cpf, cliente.email)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        print('Cliente adicionado com sucesso.')

    def dados_clientes(self):
        self.cursor.execute("SELECT nome, cpf, email FROM clientes")
        clientes = self.cursor.fetchall()
        for cliente in clientes:
            print(f"Nome: {cliente[0]}, CPF: {cliente[1]}, Email: {cliente[2]}")

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()

# Instanciando o sistema de registros
sistema = SistemaDeRegistros()

nome_cliente = input("digite seu nome:")
cpf = input("digite seu cpf:")
email = input("digite seu email:")

cliente1 = Cliente(nome_cliente, cpf, email)
sistema.registrar_cliente(cliente1)




# Listando clientes
print("Lista de Clientes:")
sistema.dados_clientes()

# Fechando a conexão
sistema.fechar_conexao()
