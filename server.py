#coding: utf-8
from sqlite3 import *

# Micros Registrados
micros = {'micro01':'192.168.1.2', 'micro02':'192.168.1.3'}

def banco():
  conex = connect('BD_Main.db')
  c = conex.cursor()
  c.execute('''CREATE TABLE if not exists clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome text,
                data_nascimento text,
                rua text,
                telefone text,
                telefone2 text,
                cidade text,
                bairro text,
                numero_casa INTEGER
            )''')
  conex.commit()
  c.close()
  return conex

# Função Desligar 
def desligar():
  import os
  global micros
  per = input('Micro: ')
  jun = micros.get(per)
  resultado = str(jun)
  print (resultado)
  os.system('shutdown /s /m \\{}'.format(resultado))
  print ('Computador {} Desligado.'.format(resultado))

# Função Bloquear
def bloquear():
        import os
        os.system('rundll32.exe user32.dll,LockWorkStation')
        print (ip + ' Bloqueado')

# Função Registro_Cliente
def registro_cliente():
        nome =str(input('Nome: ')).capitalize()
        data_nascimento = input('Data de Nascimento: ')
        rua = input('Rua: ').capitalize()
        telefone = input('Telefone/Celular: ')
        telefone2 = input('Telefone/Celular Alternativo: ')
        cidade = str(input('Cidade: ')).capitalize()
        bairro = str(input('Bairro: ')).capitalize()
        numero_casa = input('Número da Casa: ')
        print ('Registrado')
        conex = banco()
        cursor = conex.cursor()
        cursor.execute('INSERT INTO clientes VALUES('+nome+','+data_nascimento+','+rua+','+telefone+','+telefone2+','+cidade+','+bairro+','+numero_casa+')')
        conex.commit()
        cusor.close()
        
        
# Função Menu
def menu():
  while True:
                # Menu
                print ('-' * 30, 'MENU', '-' * 30);
                print("1) Abrir nova sessão \t\t\t 8) Registrar Novo Micro");
                print("2) Registrar cliente \t\t\t 9) Ver Dados de um Cliente");
                print("3) Sessões ativas");
                print("4) Desligar PC da rede");
                print("5) Bloquear computador");
                print("6) Clientes registrados");
                print("7) Sair");
                
                print ('-' * 67)
                
                # Comando:  
                comando = input("Comando: ");
                
                # Condições Menu
                if comando == "1":
                        sessao();
                elif comando == "2":
                        registro_cliente();
                elif comando == "3":
                        sessoes();
                elif comando == "4":
                        desligar();
                elif comando == "5":
                        bloquear();
                elif comando == "6":
                        clientes();
                elif comando == "7":
                        exit();
                elif comando == "8":
                        registrar_micro()
                elif comando == "9":
                        dados_cliente()
                else:
                        print ("Comando desconhecido");

# Chama a Função menu() quando o script for aberto
menu();
