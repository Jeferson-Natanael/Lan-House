from tkinter import *
import sqlite3
from CadastroUS import CadastroUS
from CadastroPC import CadastroPC
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ('arial', 10)
        self.LOGIN = StringVar()
        self.SENHA = StringVar()

        self.Top = Frame(root, bd=2,  relief=RIDGE)
        self.Top.pack(side=TOP, fill=X)
        self.Form = Frame(root, height=200)
        self.Form.pack(side=TOP, pady=20)

        self.lblTitle = Label(self.Top, text = "Autenticação para o sistema", font=('arial', 15))
        self.lblTitle.pack(fill=X)
        self.lblLOGIN = Label(self.Form, text = "LOGIN:", font=self.fontePadrao, bd=15)
        self.lblLOGIN.grid(row=0, sticky="e")
        self.lblSENHA = Label(self.Form, text = "SENHA:", font=self.fontePadrao, bd=15)
        self.lblSENHA.grid(row=1, sticky="e")
        self.lblText = Label(self.Form)
        self.lblText.grid(row=2, columnspan=2)

        self.LOGIN = Entry(self.Form, textvariable=self.LOGIN, font=(12))
        self.LOGIN.grid(row=0, column=1)
        self.SENHA = Entry(self.Form, textvariable=self.SENHA, show="*", font=(12))
        self.SENHA.grid(row=1, column=1)

        self.btnLogin = Button(self.Form, text="Login", width=45, command= self.Login)
        self.btnLogin.grid(pady=25, row=3, columnspan=2)
        self.btnLogin.bind('<Return>', self.Login)

    def Database(self):
        global conn, cursor
        conn = sqlite3.connect("banco.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS `adiministrador` (id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, login TEXT, senha TEXT)")       
        cursor.execute("SELECT * FROM `adiministrador` WHERE `login` = 'admin' AND `senha` = 'admin'")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO `adiministrador` (login, senha) VALUES('admin', 'admin')")
            conn.commit()
        
    def Login(self, event=None):
        self.Database()
        if self.LOGIN.get() == "" or self.SENHA.get() == "":
            self.lblText.config(text="Por favor, preencha o campo obrigatório!", fg="red")
        else:
            cursor.execute("SELECT * FROM `adiministrador` WHERE `login` = ? AND `senha` = ?", (self.LOGIN.get(), self.SENHA.get()))
            if cursor.fetchone() is not None:
                self.HomeWindow()
                self.LOGIN.delete(0, END)
                self.SENHA.delete(0, END)
                self.lblText.config(text="")
            else:
                self.lblText.config(text="Login ou senha invalido!", fg="red", font=self.fontePadrao)
                self.LOGIN.delete(0, END)
                self.SENHA.delete(0, END)  
        cursor.close()
        conn.close()

    def HomeWindow(self):
        global Home
        root.withdraw()
        Home = Toplevel()
        menubar = Menu(Home)
        cadastroMenu = Menu(menubar, tearoff = 0)
        cadastroMenu.add_command(label="Usuário" , command = self.cadastroUS)
        cadastroMenu.add_command(label = "Computador" , command = self.cadastroPC)
        cadastroMenu.add_separator()
        cadastroMenu.add_command(label = "Sair", command = self.Back)
        menubar.add_cascade(label = "Cadastros", menu = cadastroMenu)

        Home.config(menu = menubar)
        Home.title("SkillInfo Lan House")
        width = 600
        height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.resizable(0, 0)
        Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
        lblHome = Label(Home, text="Sistema Skillsoft", font=('times new roman', 20))
        lblHome.grid(row=0, column=0)
        lblHome.pack(fill=X)

        btnNovaSessao = Button(Home, text="Abrir nova Sessão", font=self.fontePadrao)
        # btnNovaSessao.grid(row=1,column=0)
        btnNovaSessao.pack(side=TOP)

        btnSesAtiva = Button(Home, text="Sessões Ativas", font=self.fontePadrao)
        # btnSesAtiva.grid(row=1,column=1)
        btnSesAtiva.pack(side=TOP)

        btnDeslPC = Button(Home, text="Desligar PC da Rede", font=self.fontePadrao)
        # btnDeslPC.grid(row=1,column=2)
        btnDeslPC.pack(side=TOP)

        btnBlocPC = Button(Home, text="Bloquear Computador", font=self.fontePadrao)
        # btnBlocPC.grid(row=2,column=0)
        btnBlocPC.pack(side=TOP)
        
        btnAllClientes = Button(Home, text="Todos os Clientes", font=self.fontePadrao)
        # btnAllClientes.grid(row=2,column=1)
        btnAllClientes.pack(side=TOP)


    def Back(self):
        global root
        Home.destroy()
        root.deiconify()
    
    def cadastroUS(self):
        us = CadastroUS
        us.show(self)

    def cadastroPC(self):
        pc = CadastroPC
        pc.show(self)

root = Tk()
root.title("Lan House")
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
Application(root)
root.mainloop()

# root = Tk()
# menubar = Menu(root)
# cadastroMenu = Menu(menubar, tearoff = 0)
# cadastroMenu.add_command(label="Usuário")
# cadastroMenu.add_command(label = "Computador")
# cadastroMenu.add_separator()
# cadastroMenu.add_command(label = "Sair", command = root.destroy)
# menubar.add_cascade(label = "Cadastros", menu = cadastroMenu)

# root.config(menu = menubar)
# root.title("Lan House")
# width = 400
# height = 280
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# x = (screen_width/2) - (width/2)
# y = (screen_height/2) - (height/2)
# root.geometry("%dx%d+%d+%d" % (width, height, x, y))
# root.resizable(0, 0)
# root.mainloop()

