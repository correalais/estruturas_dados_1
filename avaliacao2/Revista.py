from Publicacao import Publicacao

class Revista(Publicacao):
    def __init__(self, id, dataPubli, preco):
        super().__init__(id, dataPubli)
        self.__preco = preco
    
    def imprimeInformacoes(self):
        return super().imprimeInformacoes() + f'\nPreço: {self.__preco}'