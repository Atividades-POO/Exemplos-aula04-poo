#
# 3 - criar a class B e incluir os decoradores de acesso get e set
# para um metodo de instância possa realizar o acesso ao atributo privado e protegido
# use o decorador @property para o metodo get
# use o decorador @nomeAtributo.setter para o metodo set
# vejamos como fica a nossa classe

class B:
  def __init__(self, valor): # inicializador
    self._valor = valor # atributo privado
    self.__valor2 = valor # atributo protegido

  # get
  @property # @propperty é decorador de acesso get
  def valor(self): # método de instância
    return self._valor  # Retorna o conteudo de _valor

  @property
  def valor2(self): # método de instância
    return self.__valor2  # Retorna o valor de __valor2

  # set
  @valor.setter # @valor.setter é decorador de acesso set
  def valor(self, valor): # seta o valor do atributo _valor
    self._valor = valor # Atribui o valor ao atributo _valor

  @valor2.setter
  def valor2(self, valor): # seta o valor do atributo __valor2
    self.__valor2 = valor # Atribui o valor ao atributo __valor2