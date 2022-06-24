#
# criar a classe pessoa
class Pessoa:
  def __init__(self, nome, login = False, logoff = False): # inicializador
    self.nome = nome # atributo
    self.login = login
    self.logoff = logoff

  def logar(self):
    if self.login:
      print(f"{self.nome}, já está logado no sistema!")
      return
    print(f"Bem vindo {self.nome}, você logou no sistema.")
    self.login = True
    self.logoff = False

  def sair(self):
    if not self.login:
      print(f"{self.nome}, não está logado no sistema!")
      return
    print(f"{self.nome}, você saiu do sistema.")
    self.login = False
    self.logoff = True