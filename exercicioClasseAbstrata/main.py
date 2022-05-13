
from Notebook import Notebook
from Desktop import Desktop

desktop = Desktop('Preto', 'Asus', 5400.00, 650)

print('Desktop: \n', desktop.getInformacoes())

notebook =  Notebook('Cinza', 'Macbook Pro', 10500.00, '16h')

print('Notebook: \n', notebook.getInformacoes())