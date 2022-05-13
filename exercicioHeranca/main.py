from AlunoEnsinoMedio import AlunoEnsinoMedio
from AlunoGraduacao import AlunoGraduacao
from Cores import Cores

cor = Cores()

def registraAluno():

    nomeAluno = input(f'\n{cor.branco}Insira o nome do aluno: ')
    codAluno = int(input('Insira o Código do aluno: '))
    matAluno = int(input('Insira a Matrícula do aluno do aluno: '))


    tipoAluno = input('Este aluno é um aluno de gradução? Responda S para sim e N para não: ').upper()

    if tipoAluno == 'S':
        try:
            semAluno = int(input('Insira o semestre no qual o aluno se encontra: '))
            alunoGraduacao = AlunoGraduacao(codAluno, nomeAluno, matAluno, semAluno)
            print(alunoGraduacao)
            print (f'{cor.verde}\nCadastrado com sucesso!')
        except:
            print(f'{cor.vermelho}\nInsira apenas números! Vamos novamente!')
            registraAluno()  

    else:
        try:
            anoAluno =  int(input('Insira o ano no qual o aluno se encontra: '))
            alunoMedio = AlunoEnsinoMedio(codAluno, nomeAluno, matAluno, anoAluno)
            print(alunoMedio)
            print (f'{cor.verde}\nCadastrado com sucesso!')
        except:
            print(f'{cor.vermelho}\nInsira apenas números! Vamos novamente!')
            registraAluno()           
       
    
    

def menu():
      print( f"""\n\n {cor.rosa}                    MENU  
                    ----------------------------------
                    1. Cadastrar Aluno
                    2. Sair          
                    ----------------------------------
                    """)

def escolhas():
    escolha = input (f"{cor.rosa}Digite a opção que deseja: """)
    if escolha == '1':
         registraAluno()
    else:
        return False

while True:

    menu()
    if escolhas() == False: 
        print (f'{cor.amarelo}\nVocê escolheu finalizar.') 
        break