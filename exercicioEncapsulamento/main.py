from Fisica import Fisica
from Juridica import Juridica
from Pessoa import Pessoa

def cadastraPessoa():
    
    while True:

        nome = input('Insira o nome da pessoa que deseja cadastrar: ')
        cod =  input('Insira o código da pessoa que deseja cadastrar: ')
        end = input('Insira o endereço da pessoa que deseja cadastrar: ')
        tel = input('Insira o telefone da pessoa que deseja cadastrar: ')

        tipoPessoa = input('Insira o tipo de pessoa que deseja cadastrar: 1 para Física e 2 para Jurídica: ')

        if tipoPessoa == '1':
            cpf =  int(input('Insira o CPF da pessoa que deseja cadastrar: '))
            idade=  int(input('Insira a idade da pessoa que deseja cadastrar: '))
            peso =  float(input('Insira o peso da pessoa que deseja cadastrar: '))
            altura =  float(input('Insira a altura da pessoa que deseja cadastrar: '))

            pessoaF = Fisica(cod, nome, end, tel, cpf, idade, peso, altura)
            pessoaF.imprimeNome()
            pessoaF.getImc()

        elif tipoPessoa == '2':
            cnpj =  int(input('Insira o CNPJ da pessoa que deseja cadastrar: '))
            inscricaoEstadual=  int(input('Insira a inscrição estadual da pessoa que deseja cadastrar: '))
            qtdFunc =  int(input('Insira a quantidade de funcionarios que deseja cadastrar: '))
            pessoaJ = Juridica(cod, nome, end, tel, cnpj, inscricaoEstadual, qtdFunc)

            pessoaJ.imprimeCnpj()
            pessoaJ.getNotaFiscal()

        else:
            print('Insira uma opção válida')

        escolha = input('Deseja continuar? S para sim, N para não: ').upper()
        if escolha == 'N':
            print('\nVocê escolheu encerrar.\n')
            break


cadastraPessoa()