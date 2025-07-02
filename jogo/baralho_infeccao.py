import random
from jogo.cartas import Carta, TipoCarta
from jogo.constantes import CIDADES

class BaralhoInfeccao:
    def __init__(self):
        self.cartas = []
        self.descarte = []
        self.gerar_cartas_infeccao()

    def gerar_cartas_infeccao(self):
        for cidade, cor in CIDADES.items():
            carta = Carta(nome=cidade, tipo=TipoCarta.CIDADE, cor=cor)
            self.cartas.append(carta)
        random.shuffle(self.cartas)

    def comprar(self):
        if self.cartas:
            return self.cartas.pop(0)
        return None

    def descartar(self, carta):
        self.descarte.append(carta)

    def reciclar_descarte(self, descarte_antigo):
        self.cartas = descarte_antigo[::-1] + self.cartas
        random.shuffle(self.cartas)

    def pegar_carta_base(self):
        if self.cartas:
            return self.cartas.pop()
        return None
