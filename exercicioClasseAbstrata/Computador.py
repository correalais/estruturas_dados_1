from abc import ABCMeta, abstractmethod

class Computador(metaclass=ABCMeta):
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
    
    def getInformacoes(self):
        return f'Modelo: {self.cor}\n Cor: {self.modelo} \n Preço: {self.preco}'