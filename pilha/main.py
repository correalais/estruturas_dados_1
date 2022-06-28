from Pilha import Pilha

pilha = Pilha()

pilha.imprimirPilha()

for i in range (0, 10):
    pilha.adicionarElemento(i)

pilha.imprimirPilha()

for i in range (0, 3):
    pilha.removerDaPilha()


pilha.imprimirPilha()




