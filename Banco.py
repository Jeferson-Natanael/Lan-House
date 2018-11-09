from sqlite3 import *
class Banco():
    def __init__(self):
        self.conexao = connect('banco.db')
        self.createTable()
  
    def createTable(self):
        c = self.conexao.cursor()
  
        c.execute("""create table if not exists usuarios (
                     id integer primary key autoincrement ,
                     nome text,
                     telefone text,
                     email text,
                     login text,
                     senha text)""")
        
        c.execute("""create table if not exists computadores (
                     id integer primary key autoincrement ,
                     nome text,
                     ip text)""")
        self.conexao.commit()
        c.close()
