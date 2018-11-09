from Usuarios import Usuarios
from tkinter import *
from tkinter import ttk
from Banco import Banco
  
class CadastroUS:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
        #-----------Buscar Usuário-----------
        self.cnt2 = Frame(master)
        self.cnt2["padx"] = 20
        self.cnt2["pady"] = 5
        self.cnt2.pack()

        self.lbl = Label(self.cnt2, text="Buscar Usuário:")
        self.lbl["font"] = ("Calibri", "9", "bold")
        self.lbl.pack (side=LEFT)

        self.comb = ttk.Combobox(self.cnt2)
        self.comb.pack()
        self.comb["value"] = self.combo_input()
        self.comb.bind("<<ComboboxSelected>>", self.buscarUsuario)
        #-----------Titulo-----------
        self.cnt1 = Frame(master)
        self.cnt1["pady"] = 10
        self.cnt1.pack()

        self.titulo = Label(self.cnt1, text="Informe os dados")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        self.bntLimpar = Button(self.cnt1, text="Limpar", font=self.fonte, width=12)
        self.bntLimpar["command"] = self.limparUsuario
        self.bntLimpar.pack (side=LEFT)
        #-----------Nome do Usuário-----------
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
        #-----------Telefone do Usuário-----------
        self.cnt4 = Frame(master)
        self.cnt4["padx"] = 20
        self.cnt4["pady"] = 5
        self.cnt4.pack()

        self.lblTelefone = Label(self.cnt4, text="Telefone:", font=self.fonte, width=10)
        self.lblTelefone.pack(side=LEFT)
  
        self.txtTelefone = Entry(self.cnt4)
        self.txtTelefone["width"] = 25
        self.txtTelefone["font"] = self.fonte
        self.txtTelefone.pack(side=LEFT)
        #-----------E-mail do Usuário-----------
        self.cnt5 = Frame(master)
        self.cnt5["padx"] = 20
        self.cnt5["pady"] = 5
        self.cnt5.pack()

        self.lblEmail= Label(self.cnt5, text="E-mail:", font=self.fonte, width=10)
        self.lblEmail.pack(side=LEFT)
  
        self.txtEmail = Entry(self.cnt5)
        self.txtEmail["width"] = 25
        self.txtEmail["font"] = self.fonte
        self.txtEmail.pack(side=LEFT)
        #-----------Login do Usuário-----------
        self.cnt6 = Frame(master)
        self.cnt6["padx"] = 20
        self.cnt6["pady"] = 5
        self.cnt6.pack()
        
        self.lblLogin= Label(self.cnt6, text="Login:", font=self.fonte, width=10)
        self.lblLogin.pack(side=LEFT)
  
        self.txtLogin = Entry(self.cnt6)
        self.txtLogin["width"] = 25
        self.txtLogin["font"] = self.fonte
        self.txtLogin.pack(side=LEFT)
        #-----------Senha do Usuário-----------
        self.cnt7 = Frame(master)
        self.cnt7["padx"] = 20
        self.cnt7["pady"] = 5
        self.cnt7.pack()

        self.lblSenha= Label(self.cnt7, text="Senha:", font=self.fonte, width=10)
        self.lblSenha.pack(side=LEFT)
  
        self.txtSenha = Entry(self.cnt7)
        self.txtSenha["width"] = 25
        self.txtSenha["show"] = "*"
        self.txtSenha["font"] = self.fonte
        self.txtSenha.pack(side=LEFT)
        #-----------Comandos para o Usuário-----------
        self.cnt8 = Frame(master)
        self.cnt8["padx"] = 20
        self.cnt8["pady"] = 10
        self.cnt8.pack()

        self.bntInsert = Button(self.cnt8, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack (side=LEFT)
  
        self.bntAlterar = Button(self.cnt8, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarUsuario
        self.bntAlterar.pack (side=LEFT)
  
        self.bntExcluir = Button(self.cnt8, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirUsuario
        self.bntExcluir.pack(side=LEFT)
        #-----------Nome do Usuário-----------
        self.cnt9 = Frame(master)
        self.cnt9["pady"] = 15
        self.cnt9.pack()

        self.lblMsg = Label(self.cnt9, text="")
        self.lblMsg["font"] = ("Verdana", "9", "italic")
        self.lblMsg.pack()

    def combo_input(self):
        banco = Banco()
        c = banco.conexao.cursor()
        c.execute("select nome from usuarios")

        result = []
        for row in c.fetchall():
            result.append(row[0])
        return result

    def limparUsuario(self):
        self.comb.set('')
        self.txtNome.delete(0, END)
        self.txtTelefone.delete(0, END)
        self.txtEmail.delete(0, END)
        self.txtLogin.delete(0, END)
        self.txtSenha.delete(0, END)
                                
    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.txtNome.get()
        user.telefone = self.txtTelefone.get()
        user.email = self.txtEmail.get()
        user.login = self.txtLogin.get()
        user.senha = self.txtSenha.get()
        self.lblMsg["text"] = user.insertUser()
        self.limparUsuario()
  
    def alterarUsuario(self):
        user = Usuarios()
        user.nome = self.txtNome.get()
        user.telefone = self.txtTelefone.get()
        user.email = self.txtEmail.get()
        user.login = self.txtLogin.get()
        user.senha = self.txtSenha.get()
        self.lblMsg["text"] = user.updateUser()
        self.limparUsuario()
  
    def excluirUsuario(self):
        user = Usuarios()
        # user.idusuario = self.txtIdUsuario.get()
        self.lblMsg["text"] = user.deleteUser()
        self.limparUsuario()
  
    def buscarUsuario(self, event):
        user = Usuarios()
        nome = self.comb.get()
        if nome:
            self.lblMsg["text"] = user.selectUser(nome)

            self.txtNome.delete(0, END)
            self.txtNome.insert(INSERT, user.nome)
      
            self.txtTelefone.delete(0, END)
            self.txtTelefone.insert(INSERT,user.telefone)
      
            self.txtEmail.delete(0, END)
            self.txtEmail.insert(INSERT, user.email)
      
            self.txtLogin.delete(0, END)
            self.txtLogin.insert(INSERT, user.login)
      
            self.txtSenha.delete(0, END)
            self.txtSenha.insert(INSERT,user.senha)

    def show(self):
        root = Tk()
        root.title("Cadastro de usuário")
        width = 400
        height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)
        CadastroUS(root)
        root.mainloop()
  
  
  

