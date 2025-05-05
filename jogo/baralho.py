import random

# Classe de Baralho
class Baralho:
    def __init__(self, cartas=None):
        self.cartas = cartas or []

    def embaralhar(self):
        # Reembaralha o baralho
        random.shuffle(self.cartas)

    def tirar_carta(self):
        # Tira uma carta do baralho
        if self.cartas:
            return self.cartas.pop()
        return None

    def adicionar_carta(self, carta):
        # Adiciona uma carta ao baralho
        self.cartas.append(carta)