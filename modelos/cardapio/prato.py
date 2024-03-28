from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    """Representa uma estacia do Prato do cardapio e suas caracteristicas"""
    def __init__(self, nome, preco, descricao):
        """Inicialifa uma instãncia do Prato
        
        Herda o nome e preco da clase item_cardapio

        descricao (str): descrição do prato 
        """
        super().__init__(nome, preco)
        self.descricao = descricao
    
    def __str__(self):
        """Retorna uma representoção em string do nome do prato."""
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)