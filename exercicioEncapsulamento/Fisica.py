from Pessoa import Pessoa

class Fisica(Pessoa):

    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        super().__init__(codigo, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.imc = None
    
    def imprimeCpf(self):
        print('O CPF é: ', self.__cpf)

    def __calculaImc(self):
        imc = self.peso/(self.altura * self.altura)
        self.imc  = "{:.2f}".format(imc)
        print('O IMC da pessoa é: ', self.imc)

    def getImc(self):
       Fisica.__calculaImc(self)
        
