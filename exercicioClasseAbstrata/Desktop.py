from Computador import Computador

class Desktop(Computador):
    def __init__(self, cor, modelo, preco, potenciaDaFonte):
        super().__init__(cor, modelo, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        return super().getInformacoes() + f'\n Potencia da fonte: {self._potenciaDaFonte}'