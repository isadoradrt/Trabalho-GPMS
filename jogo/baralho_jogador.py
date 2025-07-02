from jogo.baralho import Baralho
from jogo.cartas import Carta, TipoCarta
from jogo.constantes import CIDADES
import random

class BaralhoJogador(Baralho):
    def __init__(self):
        super().__init__()
        self.gerar_cartas_jogador()
        self.embaralhar()

    def gerar_cartas_jogador(self):
        # Adiciona uma carta para cada cidade
        for nome, cor in CIDADES.items():
            self.adicionar(Carta(nome=nome, tipo=TipoCarta.CIDADE, cor=cor))

        # Duplicar 6 cartas de cidade aleatórias
        duplicadas = random.sample(list(CIDADES.items()), 6)
        for nome, cor in duplicadas:
            self.adicionar(Carta(nome=nome, tipo=TipoCarta.CIDADE, cor=cor))

        # Cartas de evento
        eventos = [
            Carta(nome="Chamas da Lamentação", tipo=TipoCarta.EVENTO, descricao="Remove 1 cubo de cada doença em qualquer lugar"),
            Carta(nome="Canção da Mãe", tipo=TipoCarta.EVENTO, descricao="Evita uma infecção"),
            Carta(nome="Escudo da Essência", tipo=TipoCarta.EVENTO, descricao="Protege uma cidade de surtos"),
            Carta(nome="Chifre Ancestral", tipo=TipoCarta.EVENTO, descricao="Dá +1 ação a um jogador")
        ]

        # Cartas de epidemia
        epidemias = [Carta(nome="Epidemia", tipo=TipoCarta.EPIDEMIA) for _ in range(3)]

        for evento in eventos:
            self.adicionar(evento)

        for epidemia in epidemias:
            self.adicionar(epidemia)

    def tirar_carta(self):
        if self.esta_vazio():
            print("O baralho de jogador está vazio!")
            return None

        carta = self.comprar()
        if carta:
            print(f"Carta tirada do baralho de jogador: {carta.nome}")
        return carta