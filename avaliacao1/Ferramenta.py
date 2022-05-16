from abc import ABCMeta, abstractmethod

class Ferramenta(metaclass=ABCMeta):
    def __init__(self, nome = None, tensao = None, preco = None):
        self.nome = nome
        self.tensao = tensao
        self.preco = preco


    @abstractmethod
    def cadastrar(self, nome, tensao, preco):
        pass

    def getInformacoes(self):
        return f'Nome da ferramenta: {self.nome}\nTensão: {self.tensao}\nPreço: {self.preco}'

