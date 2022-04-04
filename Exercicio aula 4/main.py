from Produto import Produto
from Categoria import Categoria

categoria = Categoria('Alvejante', 25)
produto = Produto('01', 'Sabão em pó', 10.90, 5.0)

produto.setCategoria(categoria)

produto.cadastrar()
