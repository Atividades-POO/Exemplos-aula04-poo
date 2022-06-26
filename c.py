
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#
#
# 4 - criar a classe Produto e usar apenas atributos publicos (nome e preço)
# crie um método desconto que retorna o valor do desconto
# depois crie os métodos get e set para os atributos
# vejamos como fica a nossa classe
#
class Produto: # classe Produto
  def __init__(self, nome, preco): # inicializador
    self.nome = nome # atributo publico
    self.preco = preco

  def desconto(self, porcentagem): # método de instância que retorna o valor do desconto
    return self.preco * (1 - porcentagem / 100) # calcula o desconto

  #get
  @property # @propperty é decorador de acesso get
  def nome(self): # método de instância que retorna o nome do produto
    return self._nome

  @property
  def preco(self): # método de instância que retorna o preço do produto
    return self._preco

  #set
  @nome.setter # @nomeAtributo.setter é decorador de acesso set
  def nome(self, valor): # seta o valor do atributo nome
    self._nome = valor

  @preco.setter
  def preco(self, valor): # seta o valor do atributo _preco
    if isinstance(valor, str): # valida se o valor é string ou não e se é string, converte para float
      valor = float(valor.replace('R$', '') .replace('.', '') .replace(',', '.')) # remove o R$ e a virgula do valor e converte para float
    self._preco = valor # atribui o valor ao atributo preco
