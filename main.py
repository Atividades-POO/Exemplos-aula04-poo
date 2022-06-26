
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#
#
# 1 - importe o arquivo pessoa.py e crie um alias para a classe Pessoa;
from pessoa import Pessoa as P
# 1.1 crie uma instância da classe pessoa
p1 = P('Davi')
# 1.2 chame o método logar duas vezes seguidas e veja as mensagens de log
p1.logar()
p1.logar()
# 1.3 chame o método sair duas vezes seguidas e veja as mensagens de log
p1.sair()
p1.sair()


#
print("-" * 20)
print()
#####################################################
# nessa parte é para entender o uso do get e set em atributos de classe

# 2 - importe o arquivo a.py
from a import A
# 2.1 crie uma instância da classe a
a1 = A(10) # cria um objeto da classe a com valor 10
# 2.2 atribua um valor ao atributo _valor
# se usamos o código abaixo o valor 10 será atribuido, mas o
# atributo _valor se trata de um atributo privado, então não
# será possível acessar o valor atribuido, potanto devemos evitar
# esse tipo de atribuição
#
# a1._valor = 10
#
# podemos usar o dir para ver os atributos da classe
print(dir(a1)) # vai imprimir os atributos da classe
# depois comente essa linha acima
#
# abaixo é a uma forma de setar o valor do atributo _valor
a1.set_valor(20) # atribui o valor 20 ao atributo _valor
# veja que o valor do atributo _valor é 20
# podemos acessar o valor do atributo _valor abaixo:
print(a1.get_valor()) # vai imprimir 20

# quando o atributo __valor2 é protegido, não podemos acessar o valor
# se tentarmos, o programa vai gerar um erro
#
# print(a1.__valor2) # vai gerar um erro
#
# especialmente, se tentarmos acessar o valor do atributo __valor2
# sem o prefixo __, o programa vai gerar um erro
# nessa situação, podemos usar o get para acessar o valor do atributo
#
a1.set_valor2(30) # atribui o valor 30 ao atributo __valor2
print(a1.get_valor2()) # vai imprimir 30
#
# existe a uma situação que podemos acessar o valor do atributo __valor2 abaixo:
# (essa forma deve ser evitado, pois, o atributo __valor2 é protegido)
# ( veremos apenas para conhecimento )
a1._A__valor2 = 40 # atribui o valor 40 ao atributo __valor2
print(a1._A__valor2) # vai imprimir 40
# é possivel ver essa forma usando o DIR da classe
print(dir(a1))  # vai imprimir os atributos da classe
# dentre os atributos da classe, podemos ver o atributo _A__valor2


#
print("-" * 20)
print()
#####################################################
# nessa parte é vamos aprender o uso do get e set em atributos de classe python
# forma correta de uso de acesso a atributos privados e protegidos em classes python
# vejamos como fica mais simplificado o acesso aos atributos privados (_b) e protegidos (__b2)
#
# 3 - importe o arquivo b.py
from b import B
# 3.1 crie uma instância da classe b
b1 = B(10) # cria um objeto da classe b com valor 10
# 3.2 atribua um valor ao atributo _b
b1.b = 20 # atribui o valor 20 ao atributo _b
# 3.3 atribua um valor ao atributo __b2
b1.b2 = 30 # atribui o valor 30 ao atributo __b2
# 3.4 veja o valor do atributo _b
print(b1.b) # vai imprimir 20
# 3.5 veja o valor do atributo __b2
print(b1.b2) # vai imprimir 30



#
print("-" * 20)
print()
#####################################################
# caso a classe já tenha atributos e que não sejam privados ou protegidos, ainda assim, podemos usar o get e set
# para acessar eles
#
# 4 - importe o arquivo c.py
from c import Produto as Pro
# 4.1 crie uma instância da classe Produto
p1 = Pro('geladeira', 1000) # cria um objeto da classe Produto com valor 1000
print(f'O produto {p1.nome} custa {p1.preco}') # vai imprimir o produto geladeira custa 1000
# calcule o desconto do produto
print(f'O produto {p1.nome}, com desconto de 10%, custa {p1.desconto(10)}') # vai imprimir o produto geladeira, com desconto de 10%, custa 900
#
# 4.2 crie uma instância da classe Produto
p2 = Pro('fogão', 500) # cria um objeto da classe Produto com valor 500
print(f'O produto {p2.nome} custa {p2.preco}') # vai imprimir o produto fogão custa 500
# calcule o desconto do produto
print(f'O produto {p2.nome}, com desconto de 5%, custa {p2.desconto(5)}') # vai imprimir o produto fogão, com desconto de 10%, custa 475

