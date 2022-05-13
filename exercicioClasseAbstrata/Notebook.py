from Computador import Computador

class Notebook(Computador):
    def __init__(self, cor, modelo, preco, tempoDeBateria):
        super().__init__(cor, modelo, preco)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        return super().getInformacoes() + f'\n Potencia da fonte: {self.__tempoDeBateria}'