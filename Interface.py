from tkinter import *
from tkinter import messagebox
from Base import *
from Desk import *

class Main:
    def __init__(self,master):
        Repositorio()        
        self.frame = Frame(master)
        self.frame.pack()

        Label(self.frame, text = "Nome").pack()
        self.nome = Entry(self.frame, width = 40)
        self.nome.pack()

        Label(self.frame, text = "Fone").pack()
        self.fone = Entry(self.frame, width = 40)
        self.fone.pack()

        Label(self.frame, text = "Setor").pack()
        self.setor = Entry(self.frame, width = 40)
        self.setor.pack()

        Label(self.frame, text = "Maquina").pack()
        self.maquina = Entry(self.frame, width = 40)
        self.maquina.pack()

        Label(self.frame, text = "Problema").pack()
        self.descricao = Entry(self.frame, width = 40)
        self.descricao.pack()

        self.separador = Frame(height = 2, bd = 3,relief = SUNKEN,width = 100)
        self.separador.pack(fill = X, pady = 5,padx = 5)

        self.frame3 = Frame(master)
        self.frame3.pack()

        self.add = Button(self.frame3,text = "adicionar", command = self.adicionar)
        self.add.pack(side = LEFT)

        self.atualizar = Button(self.frame3, text = "atualizar", command = self.atualizar)
        self.atualizar.pack(side = LEFT)
        
        scrollbar = Scrollbar(master)
        scrollbar.pack(fill = Y,side = RIGHT)
        self.listbox  = Listbox(master, width = 200, height = 50 )
        self.listbox.pack(pady = 5, padx = 5)
        self.listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = self.listbox.yview)


        #Apresentar chamados na tela ao iniciar 
        lista = Desk.mostrar(self)
        for i in lista:
            self.listbox.insert(END,i)

    def adicionar (self):
        '''nome = self.nome.get()
        fone = self.fone.get()
        setor = self.setor.get()
        maquina = self.maquina.get()
        descricao = self.descricao.get()'''
        if self.nome.get() == "" or self.fone.get() == "":
            messagebox.showwarning("Erro", "Por Favor insira Nome e Telefone")
        else:
            #uso de Herança da base de dados para adicionar no banco de dados
            Desk.adicionar(self, self.nome.get(), self.fone.get(), self.setor.get(), self.maquina.get(), self.descricao.get())

            #Limpar Caixas
            self.nome.delete(0, END)
            self.fone.delete(0,END)
            self.setor.delete(0, END)
            self.maquina.delete(0, END)
            self.descricao.delete(0, END)

            # uso de Herança da base de dados para mostas na tela ao adicionar
            lista = Desk.mostrar(self)
            self.listbox.delete(0, END)  #Limpar listbox
            for i in lista:
                self.listbox.insert(END,i)

    def atualizar (self):
        # uso de Herança da base de dados para mostas na tela
        lista = Desk.mostrar(self)
        self.listbox.delete(0, END)  #Limpar listbox
        for i in lista:
            self.listbox.insert(END, i)




root  = Tk()
root.title("Gerenciador de Chamados")
root.geometry("500x600")
Main(root)
root.mainloop()
