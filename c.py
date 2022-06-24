#
# 4 - criar a classe Produto e usar apenas atributos publicos (nome e preço)
# crie um método desconto que retorna o valor do desconto
# depois crie os métodos get e set para os atributos
# vejamos como fica a nossa classe
#
class Produto:
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco

  def desconto(self, porcentagem):
    return self.preco * (1 - porcentagem / 100) # calcula o desconto

  #get
  @property
  def nome(self):
    return self._nome

  @property
  def preco(self):
    return self._preco

  #set
  @nome.setter
  def nome(self, valor):
    self._nome = valor

  @preco.setter
  def preco(self, valor):
    if isinstance(valor, str):
      valor = float(valor.replace('R$', '') .replace('.', '') .replace(',', '.'))
    self._preco = valor
    