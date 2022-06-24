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

