from Base import *

class Desk():
    def __init__(self):
        self.conectar = sqlite3.connect('Repositorio.db')

    def adicionar(self,nome,fone,setor,maquina,descricao):
        try:
            self.conectar = sqlite3.connect('Repositorio.db')
            cursor = self.conectar.cursor()
            cursor.execute("insert into chamados values(NULL,?,?,?,?,?)", (nome, fone, setor, maquina, descricao,))
            self.conectar.commit()
            return "Chamado cadastrado!"
        except:
            return "Não foi possível realizar o cadastro do chamado"

    def mostrar(self):
        self.conectar = sqlite3.connect('Repositorio.db')
        cursor = self.conectar.cursor()
        select= cursor.execute("select * from chamados")
        self.conectar.commit()
        return select



