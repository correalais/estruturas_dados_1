from Furadeira import Furadeira
from Lixadeira import Lixadeira


def cadastroDeFuradeira():

    furadeira = Furadeira()
    
    nome = input('Digite o nome da Furadeira: ')
    tensao = input('Digite a tensão da Furadeira: ')
    preco = float(input('Digite o preço da Furadeira: '))
    potencia = input('Digite a potencia da Furadeira: ')

    furadeira.cadastrar(nome, tensao, preco, potencia)
    print('\nAs informações foram cadastradas.\n')

    print(furadeira.getInformacoes())

    
def cadastroDeLixadeira():

    lixadeira = Lixadeira()
    
    nome = input('Digite o nome da Lixadeira: ')
    tensao = input('Digite a tensão da Lixadeira: ')
    preco = float(input('Digite o preço da Lixadeira: '))
    rotacoes = input('Digite as rotações da Lixadeira: ')

    lixadeira.cadastrar(nome, tensao, preco, rotacoes)
    print('\nAs informações foram cadastradas.\n')

    print(lixadeira.getInformacoes())


def menu():
      print( f"""\n\n                   MENU  
                    ----------------------------------
                    1. Cadastrar Furadeira
                    2. Cadastrar Lixadeira
                    3. Sair          
                    ----------------------------------
                    """)

def escolhas():
    escolha = input (f"Digite a opção que deseja: """)
    if escolha == '1':
       cadastroDeFuradeira()
    if escolha == '2':
       cadastroDeLixadeira()
    else:
        return False


while True:
    menu()
    if escolhas() == False: 
        print (f'\nVocê escolheu finalizar.') 
        break