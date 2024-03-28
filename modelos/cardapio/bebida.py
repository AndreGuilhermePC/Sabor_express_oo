from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    """Representa uma estacia do Prato do cardapio e suas caracteristicas"""
    def __init__(self, nome, preco, tamanho):
        """Inicialifa uma instância de Bebida
        
        Herda o nome e preco da clase item_cardapio

        tamanho (str): informa o tamanho da bebida 
        """
        super().__init__(nome, preco)
        self.tamanho = tamanho
    
    def __str__(self):
        """Retorna uma representoção em string do nome do babida."""
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)
    
  