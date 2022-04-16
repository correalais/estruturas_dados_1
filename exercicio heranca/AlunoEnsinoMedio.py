from Aluno import Aluno

class AlunoEnsinoMedio(Aluno):

    def __init__(self, cod, nome, matricula, ano):
        super().__init__(cod, nome, matricula)
        self.ano = ano

    def __str__(self):
        return super().__str__() + f'\nAno: {self.ano}\n'