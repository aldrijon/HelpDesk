import sqlite3

class Repositorio():
    """Classe Repositorio
       Utilizada para o acesso ao Repositorio (SQLite)

       arq: Repositorio.py
    """
    def __init__(self):
        #Estabelecendo a conexão ao Repositorio de dados
        self.conectar = sqlite3.connect('Repositorio.db')
        #Criação da relação
        self.criarTabela()

    def criarTabela(self):
        #Criando o cursor para acessar o banco de dados
        cursor = self.conectar.cursor()

        #Criando relação
        cursor.execute("""create table if not exists chamados (
                     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
                     nome TEXT NOT NULL,
                     fone TEXT,
                     setor TEXT,
                     maquina TEXT,
                     descricao TEXT)"""
                    )
        #confirmando informações no banco
        self.conectar.commit()
        #fechando cursor
        cursor.close()
