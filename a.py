#
# 2 - criar a class a
class A:
  def __init__(self, valor): # inicializador
    self._valor = valor # atributo

  # get
  def get_valor(self): # método de instância
    return self._valor  # Retorna o valor da string  informada

  # set
  def set_valor(self, valor):
    self._valor = valor # Atribui o valor ao atributo
