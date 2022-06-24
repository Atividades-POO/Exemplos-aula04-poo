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