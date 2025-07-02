import random
from jogo.cartas import Carta, TipoCarta
from jogo.constantes import CIDADES, CARTAS_EPIDEMIA, CARTAS_EVENTO

class Baralho:
    def __init__(self):
        self.cartas = []
        self.descarte = []
        self.gerar_cartas()

    def gerar_cartas(self):
        for cidade, cor in CIDADES.items():
            self.cartas.append(Carta(cidade, TipoCarta.CIDADE, cor))

        for i in range(CARTAS_EVENTO):
            self.cartas.append(Carta(f"Evento {i+1}", TipoCarta.EVENTO, descricao="Ação especial"))

        for i in range(CARTAS_EPIDEMIA):
            self.cartas.append(Carta(f"Epidemia {i+1}", TipoCarta.EPIDEMIA))

        random.shuffle(self.cartas)

    def comprar(self):
        if self.cartas:
            return self.cartas.pop(0)
        return None

    def descartar(self, carta):
        self.descarte.append(carta)
