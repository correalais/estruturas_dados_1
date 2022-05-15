from ContaBancaria import ContaBancaria

class ContaPoupanca (ContaBancaria):
    def __init__(self, numConta = None, valorNaConta = 0, jurosPoup = 0):
        super().__init__(numConta, valorNaConta)
        self.jurosPoup = jurosPoup

    def cadastrar(self, numConta):
        return super().cadastrar(numConta)

    def depositar(self, valor):
        return super().depositar(valor)

    def getJurosPoup(self):
        jurosPoup = (self.valorNaConta*0.5)/100
        self.jurosPoup = "{:.2f}".format(jurosPoup)
        return self.jurosPoup

    def imprimir(self):
        return super().imprimir() + f'\nSeu juros acumulado até agora é: R$ {self.jurosPoup}'