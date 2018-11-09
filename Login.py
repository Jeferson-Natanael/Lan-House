from tkinter import*
class Login:
    def __init__(self, master=None):
##------------------- Teste manipulando click -------------------
##        self.widget1 = Frame(master)
##        self.widget1.pack()
##        self.msg = Label(self.widget1, text="Primeiro widget")
##        self.msg["font"] = ("Verdana", "10", "italic", "bold")
##        self.msg.pack()
##        self.btnSair = Button(self.widget1)
##        self.btnSair["text"] = "Click aqui"
##        self.btnSair["font"] = ("Verdana", "10")
##        self.btnSair["width"] = 10
####        self.btnSair["command"] = self.widget1.quit
####        self.btnSair.bind("<Button-1>", self.mudarTexto)
##        self.btnSair["command"] = self.mudarTexto
##        self.btnSair.pack(side=RIGHT)
##
##    def mudarTexto(self):
##        if self.msg["text"] == "Primeiro widget":
##            self.msg["text"] = "O botão recebeu um clique"
##        else:
##            self.msg["text"] = "Primeiro widget"
##--------------------------------------------------------------------
        self.fontePadrao = ("Arial", "10")
        self.Autenticado = False
        self.cnt_1 = Frame(master)
        self.cnt_1["pady"] = 10
        self.cnt_1.pack()
  
        self.cnt_2 = Frame(master)
        self.cnt_2["padx"] = 20
        self.cnt_2.pack()
  
        self.cnt_3 = Frame(master)
        self.cnt_3["padx"] = 20
        self.cnt_3.pack()
  
        self.cnt_4 = Frame(master)
        self.cnt_4["pady"] = 20
        self.cnt_4.pack()
  
        self.titulo = Label(self.cnt_1, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.cnt_2,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.cnt_2)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
        
        self.senhaLabel = Label(self.cnt_3, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
  
        self.senha = Entry(self.cnt_3)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)
  
        self.autenticar = Button(self.cnt_4)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()
  
        self.mensagem = Label(self.cnt_4, text="", font=self.fontePadrao)
        self.mensagem.pack()
  
    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "jeferson" and senha == "1234":
            self.mensagem["text"] = "Autenticado"
            self.Autenticado = True
            self.master.deiconify()
        else:
            self.mensagem["text"] = "Erro na autenticação"
            self.Autenticado = False

##root = Tk()
##Application(root)
##root.mainloop()
