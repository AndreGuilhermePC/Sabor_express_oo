from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('praça', 'gourmet')
#restaurante_mexicano = Restaurante('mexican food', 'mexicana')
#restaurante_japonesa = Restaurante('jata', 'japonesa')

#restaurante_mexicano.alterna_estado()

#restaurante_praca.receber_avaliacao('Gui', 10)
#restaurante_praca.receber_avaliacao('Lais', 8)
#restaurante_praca.receber_avaliacao('Emy', 2)

bebida_suco = Bebida('Suco de Mel', 5.0, 'Grande')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.0, 'O melhor pão da cidade')
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
prato_paozinho.aplicar_desconto()

def main():
    print(restaurante_praca.lista_restaurante())
    print()
    restaurante_praca.exibir_cardapio

if __name__=='__main__':
    main()