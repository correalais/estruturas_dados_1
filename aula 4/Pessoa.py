class Pessoa:

    def __init__(self, nome = None, telefone = None, salario = None, cid = None):
        self.nome = nome
        self.telefone = telefone
        self.salario = salario
        self.municipio = cid

    def cadastrar(self):
        print ('\nNome: ', self.nome)
        print ('\nTelefone: ', self.telefone)
        print ('\nSalario: ', self.salario)
        print ('\nCidade: ', self.municipio.nome, '/', self.municipio.estado)
        print ('\nCadastro realizado')