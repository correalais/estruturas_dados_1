class Aluno:

    def __init__(self, cod, nome, matricula):
        self.cod = cod
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f'\nNome: {self.nome} \nCódigo: {self.cod} \nMatrícula: {self.matricula}'