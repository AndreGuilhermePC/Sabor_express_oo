from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamaho):
        super().__init__(nome, preco)
        self._tamanho = tamaho
    
    def __str__(self):
        return self._nome