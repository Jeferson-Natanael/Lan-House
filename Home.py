from tkinter import *
import sqlite3

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

def Database():
    global conn, cursor
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `adiministrador` (id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, login TEXT, senha TEXT)")       
    cursor.execute("SELECT * FROM `adiministrador` WHERE `login` = 'admin' AND `senha` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `adiministrador` (login, senha) VALUES('admin', 'admin')")
        conn.commit()
    
def Login(event=None):
    Database()
    if LOGIN.get() == "" or SENHA.get() == "":
        lbl_text.config(text="Por favor, preencha o campo obrigatório!", fg="red")
    else:
        cursor.execute("SELECT * FROM `adiministrador` WHERE `login` = ? AND `senha` = ?", (LOGIN.get(), SENHA.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            LOGIN.delete(0, END)
            SENHA.delete(0, END)
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Login ou senha invalido!", fg="red")
            LOGIN.delete(0, END)
            SENHA.delete(0, END)  
    cursor.close()
    conn.close()

def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    menubar = Menu(Home)
    cadastroMenu = Menu(menubar, tearoff = 0)
    cadastroMenu.add_command(label="Usuário")
    cadastroMenu.add_command(label = "Computador")
    cadastroMenu.add_separator()
    cadastroMenu.add_command(label = "Sair", command = root.destroy)
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
    lbl_home = Label(Home, text="Logado com sucesso!", font=('times new roman', 20)).pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)

def Back():
    Home.destroy()
    root.deiconify()

LOGIN = StringVar()
SENHA = StringVar()

Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)

lbl_title = Label(Top, text = "Autenticação para o sistema", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_LOGIN = Label(Form, text = "LOGIN:", font=('arial', 14), bd=15)
lbl_LOGIN.grid(row=0, sticky="e")
lbl_SENHA = Label(Form, text = "SENHA:", font=('arial', 14), bd=15)
lbl_SENHA.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

LOGIN = Entry(Form, textvariable=LOGIN, font=(14))
LOGIN.grid(row=0, column=1)
SENHA = Entry(Form, textvariable=SENHA, show="*", font=(14))
SENHA.grid(row=1, column=1)

btn_login = Button(Form, text="Login", width=45, command=Login)
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', Login)

##root = Tk()
##menubar = Menu(root)
##cadastroMenu = Menu(menubar, tearoff = 0)
##cadastroMenu.add_command(label="Usuário", command = cadastro_usuario)
##cadastroMenu.add_command(label = "Computador", command = cadastro_computador)
##cadastroMenu.add_separator()
##cadastroMenu.add_command(label = "Sair", command = root.destroy)
##menubar.add_cascade(label = "Cadastros", menu = cadastroMenu)
##
##root.config(menu = menubar)
##root.title("Lan House")
##width = 400
##height = 280
##screen_width = root.winfo_screenwidth()
##screen_height = root.winfo_screenheight()
##x = (screen_width/2) - (width/2)
##y = (screen_height/2) - (height/2)
##root.geometry("%dx%d+%d+%d" % (width, height, x, y))
##root.resizable(0, 0)
##root.mainloop()

