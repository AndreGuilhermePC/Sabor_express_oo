from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
#restaurante_mexicano = Restaurante('mexican food', 'mexicana')
#restaurante_japonesa = Restaurante('jata', 'japonesa')

#restaurante_mexicano.alterna_estado()

restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 2)

def main():
    Restaurante.lista_restaurante()

if __name__=='__main__':
    main()