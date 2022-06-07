from No import No

class Lista:
    def __init__(self):
        self.primeiro = None

    def insereInicio(self, valor):
        novoNo = No(valor)
        novoNo.proximo = self.primeiro
        self.primeiro = novoNo

    def mostrar(self):
        atual = self.primeiro
        while atual != None:
            atual.mostraNo()
            atual = atual.proximo


    def excluirInicio (self):
        temp = self.primeiro
        if self.primeiro.proximo == None:
            return None
        self.primeiro = self.primeiro.proximo
        return temp