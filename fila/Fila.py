from No import No

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def inserir(self, valor):
        novoNo = No(valor)
        if self.inicio == None:
            self.inicio = novoNo
            self.fim = novoNo
        else:
            self.fim.proximo = novoNo
            self.fim = novoNo            
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        if self.inicio == None:
            print("A fila está vazia!")
        else:
            print("\n---------------------\n")
            aux = self.inicio
            while aux != None:
                print(aux.valor)
                aux = aux.proximo
            print("\nTamanho da fila: ", self.tamanho)
    
    def remover(self):
        if self.inicio == None:
            print ('A fila está vazia')
        else:
            if self.tamanho == 1:
                self.inicio = None
                self.fim = None
                self.tamanho = 0
            else:
                self.inicio = self.inicio.proximo
                self.tamanho -= 1
            self.imprimir()
