from ContaBancaria import ContaBancaria

class ContaCorrente (ContaBancaria):
    def __init__(self, numConta = None, valorNaConta = 0, chavePix = None):
        super().__init__(numConta, valorNaConta)
        self.chavePix = chavePix

    def cadastrar(self, numConta):
        return super().cadastrar(numConta)

    def depositar(self, valor):
        return super().depositar(valor)

    def cadastrarPix(self, chavePix):
        self.chavePix = chavePix
        return chavePix

    def imprimir(self):
        return super().imprimir() + f'\nSua chave pix é: {self.chavePix}'