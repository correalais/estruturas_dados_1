from Publicacao import Publicacao

class Livro(Publicacao):
    def __init__(self, id, dataPubli, titulo, autor):
        super().__init__(id, dataPubli)
        self.titulo = titulo
        self._autor = autor
    
    def imprimeInformacoes(self):
        return super().imprimeInformacoes() + f'\nTítulo: {self.titulo} \nAutor: {self._autor}'