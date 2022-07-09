class Publicacao:
    def __init__(self, id, dataPubli):
        self.id = id
        self.dataPubli = dataPubli

    def imprimeInformacoes(self):
        return f'\nID: {self.id} \nData: {self.dataPubli}'