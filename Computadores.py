from Banco import Banco
  
class Computadores(object):
    def __init__(self, idpc = 0, nome = "", ip = ""):
        self.idpc = idpc
        self.nome = nome
        self.ip = ip
  
    def insertPC(self):
  
        banco = Banco()
        try:
  
            c = banco.conexao.cursor()
  
            c.execute("insert into computadores (nome, ip) values ('" +
                      self.nome + "', '" + self.ip + "' )")
  
            banco.conexao.commit()
            c.close()
  
            return "Computador cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do computador"
  
    def updatePC(self):
  
        banco = Banco()
        try:
  
            c = banco.conexao.cursor()
  
            c.execute("update computadores set nome = '" + self.nome + "', ip = '" + self.ip +
                      "' where idpc = " + self.idpc + " ")
  
            banco.conexao.commit()
            c.close()
  
            return "Computador atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do computador"
  
    def deletePC(self):
  
        banco = Banco()
        try:
  
            c = banco.conexao.cursor()
  
            c.execute("delete from computadores where id = " + self.idpc + " ")
  
            banco.conexao.commit()
            c.close()
  
            return "Computador excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do computador"
  
    def selectPC(self, idpc):
        banco = Banco()
        try:
  
            c = banco.conexao.cursor()
            c.execute("select * from computadores where nome ='" + idpc + "'  ")
            
            for linha in c:
                self.idpc = linha[0]
                self.nome = linha[1]
                self.ip = linha[4]
            if self.idpc == 0:
                c.close()
                return "Nenhum computador encontrado!"
                
            c.close()
  
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do computador"
