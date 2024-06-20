import mysql.connector  # importação da biblioteca que é usada para interagir com o banco de dados

class Clientes: # criação da classe "cliente"
    def __init__(self, nome, cpf): # definindo a inicialização da classe e os atributos
        self.nome = nome # está atribuindo o valor do parametro "nome" para ao atributo "self.nome"
        self.cpf = cpf 
class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class SistemaDeProdutos: 
    def __init__(self): 
        self.conexao = mysql.connector.connect( 
            host="localhost", 
            user="root", 
            password="he182555@", 
            database="lojinha"
        )
        self.cursor = self.conexao.cursor()

    def cadastrar_cliente(self, cliente): 
        sql = "INSERT INTO clientes (nome, cpf) VALUES (%s, %s)" 
        valores = (cliente.nome, cliente.cpf)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        
    def adicionar_produto(self, produto): 
        sql = "INSERT INTO produtos (nome, preco) VALUES (%s, %s)" 
        valores = (produto.nome, produto.preco)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        

    def listar_produtos(self):
        self.cursor.execute("SELECT nome, preco FROM produtos")
        produtos = self.cursor.fetchall() 
        for produto in produtos: 
            print(f"Nome: {produto[0]}, preco: {produto[1]}") 

    def fechar_conexao(self): 
        self.cursor.close() 
        self.conexao.close() 


sistema = SistemaDeProdutos()


cliente1 = Clientes("Dhario", "45673233")
cliente2 = Clientes("Pedro", "23435678")

sistema.cadastrar_cliente(cliente1)
sistema.cadastrar_cliente(cliente2)

produto1 = Produtos("garrafa", '50')

sistema.adicionar_produto(produto1)

input("Digite seu nome:")
input("Digite seu cpf:")
print("Cliente cadastrado")




print("Lista de produtos:")
sistema.listar_produtos()

sistema.fechar_conexao()









