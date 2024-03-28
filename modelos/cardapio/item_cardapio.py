from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    """Represeta os item do cardapio e suas caracteristicas"""
    def __init__(self, nome, preco):
        """
        Inicialifa uma instância do item cardapio

        - nome (str): nome do item
        - preco (float): valor do item 
        """
        self._nome = nome
        self._preco = preco
    
    @abstractmethod
    def aplicar_desconto(self):
        pass