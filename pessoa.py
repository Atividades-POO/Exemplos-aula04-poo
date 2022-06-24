#
# 1 - criar a classe pessoa
class Pessoa:
  def __init__(self, nome, login = False, logoff = False): # inicializador
    self.nome = nome # atributo
    self.login = login
    self.logoff = logoff

  def logar(self): # método de instância
    if self.login:  # se estiver logado
      print(f"{self.nome}, já está logado no sistema!")  # imprime mensagem
      return # sai do método logar
    self.login = True  # loga no sistema e imprime mensagem
    print(f"Bem vindo {self.nome}, você logou no sistema.") # se não estiver logado
    self.logoff = False # não está logado no sistema

  def sair(self): # método de instância
    if not self.login: # se não estiver logado
      print(f"{self.nome}, não está logado no sistema!") # imprime mensagem e sai do método
      return # sai do método sair
    self.login = False  # não está logado no sistema e imprime mensagem
    print(f"{self.nome}, você saiu do sistema.") # se estiver logado
    self.logoff = True # está logado no sistema