listaProdutos = ['arroz', 'feijao', 'batata', 'pizza']
listaPreco = [3.89, 4.80, 2.50, 12.50]
listaQnt = [25, 20, 60, 10]

def imprimeListaCompleta():

    for i in range (len(listaProdutos)):
         print('Produto: ', listaProdutos[i], ' | Preço: ', listaPreco[i], ' | Quantidade disponível: ', listaQnt[i])



def escolhaProdutos():
    

    while True:        

        escolha = input('\nEscolha uma opção: 1 para consultar produtos | 2 para remover produtos | 3 para ver a lista completa de Produtos | Outra tecla para sair: \n')
        
        if escolha =='1':

            produto = input('\nInsira o nome do produto que deseja ver o preço e quantidade: ')
            imprimeProd(produto)


        elif escolha =='2':
            produto = input('\nInsira o nome do produto que deseja remover: ')
            removeProdutos(produto)

        
        elif escolha =='3':
            imprimeListaCompleta()

        else:
            print('\nPrograma encerrado.')
            break


def removeProdutos(produto):
    if produto in listaProdutos:
        ind = listaProdutos.index(produto)
        listaProdutos.pop(ind)
        listaPreco.pop(ind)
        listaQnt.pop(ind)
        print('\nLista atualizada dos produtos: ')

        for i in range (len(listaProdutos)):
            print('\nProduto: ', listaProdutos[i], ' | Preço: ', listaPreco[i], ' | Quantidade disponível: ', listaQnt[i])
    else:
        print('\nProduto não consta na lista!')

    



def imprimeProd(produto):
    if produto in listaProdutos:
        ind = listaProdutos.index(produto)
        print('\nProduto: ', produto, ' | Preço: ', listaPreco[ind], ' | Quantidade disponível: ', listaQnt[ind])
    else:
        print('\nProduto não consta na lista!')



escolhaProdutos()

