from baralho import Baralho

class BaralhoJogador(Baralho):
    def __init__(self, cartas=None):
        super().__init__(cartas)

    def tirar_carta(self):
        if not self.cartas:  
            print("O baralho de jogador está vazio!")
            return None  

        carta = super().tirar_carta()  
        if carta:
            print(f"Carta do baralho de jogador tirada!")
        return carta