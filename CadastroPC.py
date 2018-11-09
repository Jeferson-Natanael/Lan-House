from Computadores import Computadores
from tkinter import *
from tkinter import ttk
from Banco import Banco
  
class CadastroPC:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
        #-----------Buscar PC's-----------
        self.cnt2 = Frame(master)
        self.cnt2["padx"] = 20
        self.cnt2["pady"] = 5
        self.cnt2.pack()

        self.lbl = Label(self.cnt2, text="Buscar PC's:")
        self.lbl["font"] = ("Calibri", "9", "bold")
        self.lbl.pack (side=LEFT)

        self.comb = ttk.Combobox(self.cnt2)
        self.comb.pack()
        self.comb["value"] = self.combo_input()
        self.comb.bind("<<ComboboxSelected>>", self.buscarComputador)
        #-----------Titulo-----------
        self.cnt1 = Frame(master)
        self.cnt1["pady"] = 10
        self.cnt1.pack()

        self.titulo = Label(self.cnt1, text="Informe os dados")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        self.bntLimpar = Button(self.cnt1, text="Limpar", font=self.fonte, width=12)
        self.bntLimpar["command"] = self.limparComputador
        self.bntLimpar.pack (side=LEFT)
        #-----------Nome do Computador-----------
        self.cnt3 = Frame(master)
        self.cnt3["padx"] = 20
        self.cnt3["pady"] = 5
        self.cnt3.pack()

        self.lblNome = Label(self.cnt3, text="Nome:", font=self.fonte, width=10)
        self.lblNome.pack(side=LEFT)
  
        self.txtNome = Entry(self.cnt3)
        self.txtNome["width"] = 25
        self.txtNome["font"] = self.fonte
        self.txtNome.pack(side=LEFT)
        #-----------IP do Computador-----------
        self.cnt4 = Frame(master)
        self.cnt4["padx"] = 20
        self.cnt4["pady"] = 5
        self.cnt4.pack()
        
        self.lblIP= Label(self.cnt4, text="IP:", font=self.fonte, width=10)
        self.lblIP.pack(side=LEFT)
  
        self.txtIP = Entry(self.cnt4)
        self.txtIP["width"] = 25
        self.txtIP["font"] = self.fonte
        self.txtIP.pack(side=LEFT)
        #-----------Comandos para o Computador-----------
        self.cnt5 = Frame(master)
        self.cnt5["padx"] = 20
        self.cnt5["pady"] = 10
        self.cnt5.pack()

        self.bntInsert = Button(self.cnt5, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirComputador
        self.bntInsert.pack (side=LEFT)
  
        self.bntAlterar = Button(self.cnt5, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarComputador
        self.bntAlterar.pack (side=LEFT)
  
        self.bntExcluir = Button(self.cnt5, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirComputador
        self.bntExcluir.pack(side=LEFT)
        #-----------MSG do Comando-----------
        self.cnt6 = Frame(master)
        self.cnt6["pady"] = 15
        self.cnt6.pack()

        self.lblMsg = Label(self.cnt6, text="")
        self.lblMsg["font"] = ("Verdana", "9", "italic")
        self.lblMsg.pack()

    def combo_input(self):
        banco = Banco()
        c = banco.conexao.cursor()
        c.execute("select nome from computadores")

        result = []
        for row in c.fetchall():
            result.append(row[0])
        return result

    def limparComputador(self):
        self.comb.set('')
        self.txtNome.delete(0, END)
        self.txtIP.delete(0, END)
                                
    def inserirComputador(self):
        pc = Computadores()
        pc.nome = self.txtNome.get()
        pc.ip = self.txtIP.get()
        self.lblMsg["text"] = pc.insertPC()
        self.limparComputador()
  
    def alterarComputador(self):
        pc = Computadores()
        pc.nome = self.txtNome.get()
        pc.ip = self.txtIP.get()
        self.lblMsg["text"] = pc.updatePC()
        self.limparComputador()
  
    def excluirComputador(self):
        pc = Computadores()
        nome = self.comb.get()
        pc.nome = nome
        self.lblMsg["text"] = pc.deletePC()
        self.limparComputador()


    def buscarComputador(self, event):
        pc = Computadores()
        nome = self.comb.get()
        if nome:
            self.lblMsg["text"] = pc.selectPC(nome)

            self.txtNome.delete(0, END)
            self.txtNome.insert(INSERT, pc.nome)
      
            self.txtIP.delete(0, END)
            self.txtIP.insert(INSERT, pc.ip)
  
    def show(self):
        root = Tk()
        root.title("Cadastro de computador")
        width = 400
        height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)
        CadastroPC(root)
        root.mainloop()
