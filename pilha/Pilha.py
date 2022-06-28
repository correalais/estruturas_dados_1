from No import No

class Pilha:    
	def __init__(self):
		self.topoDaPilha = None
		self.tamanho = 0

	def adicionarElemento(self, valor) :
		novoNo = No(valor)
		if self.topoDaPilha == None:
			self.topoDaPilha = novoNo
		else:
			novoNo.proximo = self.topoDaPilha
			self.topoDaPilha = novoNo
		self.tamanho += 1

	
	def imprimirPilha(self) :
		if self.topoDaPilha == None:
			print('\nA Pilha está vazia.\n')
		else:
			aux = self.topoDaPilha
			while(aux != None) :
				print(aux.valor, '\n' )
				aux = aux.proximo
			print('\nTamanho da Pilha: ', self.tamanho, '\n')
	
	def removerDaPilha(self):
		if self.topoDaPilha == None:
			print('\nA Pilha está vazia.\n')
		elif self.topoDaPilha.proximo == None:
			self.topoDaPilha = None
			self.tamanho = 0
		else:
			self.topoDaPilha = self.topoDaPilha.proximo
			self.tamanho -= 1