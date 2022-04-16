from Aluno import Aluno

class AlunoGraduacao(Aluno):

    def __init__(self, cod, nome, matricula, semestre):
        super().__init__(cod, nome, matricula)
        self.semestre = semestre

    def __str__(self):
        return super().__str__() + f'\nSemestre: {self.semestre}\n'