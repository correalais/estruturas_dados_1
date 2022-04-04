class Produto:
    def __init__(self, cod = None, nome = None, preco = 0.0, qnt = 0):

        self.codigo = cod
        self.nome = nome
        self.preco = preco
        self.qnt = qnt
        self.cat = None

    def setCategoria(self, cat):
        self.cat = cat

    def cadastrar(self):
        print('Código do produto: ', self.codigo)
        print('Nome: ', self.nome)
        print('Preço: ', self.preco)
        print('Quantidade: ', self.qnt)
        print('Categoria: ', self.cat)