class Categoria:

    def __init__(self, nomeC = "Sem nome", cod = 0):
        self.nome = nomeC
        self.cod = cod

    def cadastrar(self):
        print ('A categoria é: ', self.nome)
        print ('O Código é: ', self.cod)

    def __str__(self):
        return f" Código: {str(self.cod) + ' - ' + self.nome}"