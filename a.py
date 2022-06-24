#
# 2 - criar a class A
class A:
  def __init__(self, valor): # inicializador
    self._valor = valor # atributo privado
    self.__valor2 = valor # atributo protegido

  # get
  def get_valor(self): # método de instância
    return self._valor  # Retorna o conteudo de _valor

  def get_valor2(self): # método de instância
    return self.__valor2  # Retorna o valor de __valor2

  # set
  def set_valor(self, valor): # seta o valor do atributo _valor
    self._valor = valor # Atribui o valor ao atributo _valor

  def set_valor2(self, valor): # seta o valor do atributo __valor2
    self.__valor2 = valor # Atribui o valor ao atributo __valor2