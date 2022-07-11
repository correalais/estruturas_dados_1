precoAtual = [150.90, 99.90, 49.99, 12.50]

def insereDesconto (precoAtual):
    return precoAtual - (precoAtual * 0.50)

listaDeDescontos = list(map(insereDesconto, precoAtual))

print ('\nOs valores originais sem desconto são: ', precoAtual)

print('\nOs valores com 50% de desconto são: ', listaDeDescontos, '\n')

