#
# 3 - criar a class B e incluir os decoradores de acesso get e set
# para um metodo de instância possa realizar o acesso ao atributo privado e protegido
# use o decorador @property para o metodo get
# use o decorador @nomeAtributo.setter para o metodo set
# vejamos como fica a nossa classe

class B:
  def __init__(self, valor): # inicializador
    self._b = valor # atributo privado
    self.__b2 = valor # atributo protegido

  # get
  @property # @propperty é decorador de acesso get
  def b(self): # método de instância
    return self._b  # Retorna o conteudo de _b

  @property
  def b2(self): # método de instância
    return self.__b2  # Retorna o valor de __b2

  # set
  @b.setter # @nomeAtributo.setter é decorador de acesso set
  def b(self, valor): # seta o valor do atributo _valor
    self._b = valor # Atribui o valor ao atributo _b

  @b2.setter
  def b2(self, valor): # seta o valor do atributo __b2
    self.__b2 = valor # Atribui o valor ao atributo __b2