from FilaCliente import FilaCliente
from Cliente import Cliente


fila = FilaCliente()
cliente1 = Cliente('José', 42)
cliente2 = Cliente('Maria', 32)
cliente3 = Cliente('Joaquina', 27)


fila.inserir(cliente1)
fila.inserir(cliente2)
fila.inserir(cliente3)

fila.remover()