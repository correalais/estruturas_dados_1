class Pessoa:

    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = codigo
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone

    def imprimeNome(self):
        print ('O nome da pessoa é: ', self.nome)

    def __imprimeTelefone(self):
        print('O telefone da pessoa é: ', self.__telefone)