import mysql.connector 

class Alunos:
    def __init__(self, nome, cpf): 
        self.nome = nome 
        self.cpf = cpf 

class Sistema_escolar: 
    def __init__(self): 
        self.conexao = mysql.connector.connect( 
            host="localhost", 
            user="root", 
            password="he182555@", 
            database="escola_tecnica"
        )
        self.cursor = self.conexao.cursor()

    def matricular_aluno(self, aluno): 
        sql = "INSERT INTO alunos (nome, cpf) VALUES (%s, %s)" 
        valores = (aluno.nome, aluno.cpf)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        print('Aluno adicionado com sucesso.')

    def listar_alunos(self):
        self.cursor.execute("SELECT nome, cpf FROM alunos")
        alunos = self.cursor.fetchall() 
        for aluno in alunos: 
            print(f"Nome: {aluno[0]}, CPF: {aluno[1]}") 

    def fechar_conexao(self): 
        self.cursor.close() 
        self.conexao.close() 


sistema = Sistema_escolar() 


aluno1 = Alunos('Henrique', "45673233")
aluno2 = Alunos('Ana', "23435678")


sistema.matricular_aluno(aluno1)
sistema.matricular_aluno(aluno2)


print("Lista de Alunos: ")
sistema.listar_alunos()


sistema.fechar_conexao()





