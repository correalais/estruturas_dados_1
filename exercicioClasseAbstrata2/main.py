from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

contaCorrente = ContaCorrente()
contaCorrente.cadastrar('12345 - 6')
contaCorrente.depositar(2541.60)
contaCorrente.cadastrarPix('51 999887766')

print(contaCorrente.imprimir())

print ('\n----------------------------\n')

contaPoupanca = ContaPoupanca()
contaPoupanca.cadastrar('56789 - 0')
contaPoupanca.depositar(2752.32)
contaPoupanca.getJurosPoup()

print(contaPoupanca.imprimir())
