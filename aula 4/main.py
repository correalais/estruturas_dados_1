from Pessoa import Pessoa
from Cidade import Cidade

c1 = Cidade('Porto Alegre', 'RS')
p1 = Pessoa('Fulano de tal', '5464654', 12584.0, c1)


p1.cadastrar()

print ('---------------')
p2 = Pessoa('Fulana', '5464848', 78645.0, c1 )
p2.cadastrar()