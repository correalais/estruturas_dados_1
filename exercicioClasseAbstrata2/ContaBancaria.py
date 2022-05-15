from abc import ABCMeta, abstractmethod

class ContaBancaria(metaclass=ABCMeta):
    def __init__(self, numConta = None, valorNaConta = 0):
        self.numConta = numConta
        self.valorNaConta = valorNaConta

    def cadastrar(self, numConta):
        self.numConta = numConta
        return self.numConta

    def depositar(self, valor):
        self.valorNaConta = self.valorNaConta + valor
        return self.valorNaConta

    def imprimir(self):
        return f'O número da sua conta é: {self.numConta}\nSeu saldo atual é: R$ {self.valorNaConta} '