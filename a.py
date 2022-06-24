#
# criar a class a
class A:
  def __init__(self, valor):
    self._valor = valor
  def get_valor(self):
    return self._valor  # Retorna o valor da string  informada
  def set_valor(self, valor):
    self._valor = valor # Atribui o valor ao atributo
