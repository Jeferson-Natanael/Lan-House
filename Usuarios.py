from Banco import Banco
  
class Usuarios(object):
    def __init__(self, idusuario = 0, nome = "", telefone = "",
                 email = "", login = "", senha = ""):
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.login = login
        self.senha = senha
  
  
    def insertUser(self):
  
        banco = Banco()
        try:
  
            c = banco.conexao.cursor()
  
            c.execute("insert into usuarios (nome, telefone, email, login, senha) values ('" +
                      self.nome + "', '" + self.telefone + "', '" + self.email + "', '" +
                      self.login + "', '" + self.senha + "' )")
  
            banco.conexao.commit()
            c.close()
  
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"
  
    def updateUser(self):
  
        banco = Banco()
        try:
  
            c = banco.conexao.cursor()
  
            c.execute("update usuarios set nome = '" + self.nome + "', telefone = '" +
                      self.telefone + "', email = '" + self.email + "', login = '" + self.login +
                      "', senha = '" + self.senha + "' where idusuario = " + self.idusuario + " ")
  
            banco.conexao.commit()
            c.close()
  
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"
  
    def deleteUser(self):
  
        banco = Banco()
        try:
  
            c = banco.conexao.cursor()
  
            c.execute("delete from usuarios where id = " + self.idusuario + " ")
  
            banco.conexao.commit()
            c.close()
  
            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"
  
    def selectUser(self, idusuario):
        banco = Banco()
        try:
  
            c = banco.conexao.cursor()
            c.execute("select * from usuarios where nome ='" + idusuario + "'  ")
            
            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.login = linha[4]
                self.senha = linha[5]
            if self.idusuario == 0:
                c.close()
                return "Nenhum usuário encontrado!"
                
            c.close()
  
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"
