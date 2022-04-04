

class calculaRetangulo:

    def __init__(self):
        self.altura = 0
        self.largura = 0
        self.area = 0

    def calculaArea(self, altura, largura):

        self.altura = altura
        self.largura = largura
        self.area = self.altura * self.largura
        return self.area

    def imprimeResultado(self):
        
        print('A área é: ', self.area)

retangulo = calculaRetangulo()

altura = int(input('Insira a altura para calcular a área: '))
largura = int(input('Insira a largura para calcular a área: '))

retangulo.calculaArea(altura, largura)
retangulo.imprimeResultado()