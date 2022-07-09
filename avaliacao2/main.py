from Livro import Livro
from Revista import Revista
from Pilha import Pilha

pilhaLivros = Pilha()
pilhaRevistas = Pilha()

def adicionaLivro():
    id = input('Insira o ID do livro: ')
    data = input('Insira a data de publicação do livro: ')
    titulo = input('Insira o titulo do livro: ')
    autor = input('Insira o autor do livro: ')
    livro = Livro(id, data, titulo, autor)
    
    pilhaLivros.adicionarElemento(livro)
    print('\nLivro cadastrado com sucesso.')

def adicionaRevista():
    id = input('Insira o ID da revista: ')
    data = input('Insira a data de publicação da revista: ')
    preco = float(input('Insira o preço da revista: '))
    revista = Revista(id, data, preco)

    pilhaRevistas.adicionarElemento(revista)
    print('\nRevista cadastrada com sucesso.')


def removerLivros():
    pilhaLivros.removerDaPilha()
    print('\nO livro que era topo da pilha foi removido.')

def imprimeLivros():
    print('Livros cadastrados: \n')
    pilhaLivros.imprimirPilha()

def imprimeRevistas():
    print('Revistas cadastradas: \n')
    pilhaRevistas.imprimirPilha()

def removerRevistas():
    pilhaRevistas.removerDaPilha()
    print('\nA revista que era topo da pilha foi removida.')

def menu():
    while True:
        escolha = input( f"""\n\n          Insira a opção desejada:  
                        ----------------------------------
                        1. Adicionar Livros
                        2. Adicionar Revistas   
                        3. Remover Livros
                        4. Remover Revistas
                        5. Imprimir Pilha de Livros
                        6. Imprimir Pilha de Revistas 
                        7. Sair      
                        ----------------------------------
                        """)
        if escolha == '1':
            adicionaLivro()
        elif escolha == '2':
           adicionaRevista()
        elif escolha == '3':
            removerLivros()
        elif escolha == '4':
            removerRevistas()
        elif escolha == '5':
            imprimeLivros()
        elif escolha == '6':
            imprimeRevistas()
        else:
            print(f'\nVocê escolheu sair.')
            break

menu()