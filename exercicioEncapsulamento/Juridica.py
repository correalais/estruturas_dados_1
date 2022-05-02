from Pessoa import Pessoa

class Juridica(Pessoa):

    def __init__(self, codigo, nome, endereco, telefone, cnpj, inscricaoEstadual, quantidadeFuncionarios):
        super().__init__(codigo, nome, endereco, telefone)
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.quantidadeFuncionarios = quantidadeFuncionarios

    
    def imprimeCnpj(self):
        print('O CNPJ é: ', self.__cnpj)

    def __emitirNotaFiscal(self):
       print('Nota Fiscal emitida.')

    def getNotaFiscal(self):
        Juridica.__emitirNotaFiscal(self)