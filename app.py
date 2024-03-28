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
prato_paozinho = Prato('Paozinho', 2.0, 'O melhor pão da cidade')

def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__=='__main__':
    main()