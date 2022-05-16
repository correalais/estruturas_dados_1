from Ferramenta import Ferramenta

class Lixadeira(Ferramenta):
    def __init__(self, nome = None, tensao = None, preco = None, rotacoes = None):
        super().__init__(nome, tensao, preco)
        self.__rotacoes = rotacoes

    def cadastrar(self, nome, tensao, preco, rotacoes):
        self.nome = nome
        self.tensao = tensao
        self.preco = preco
        self.__rotacoes = rotacoes

    def getInformacoes(self):
        return super().getInformacoes() + f'\nRotações: {self.__rotacoes}'